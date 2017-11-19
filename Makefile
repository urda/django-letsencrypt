########################################################################################################################
# Variables
########################################################################################################################

BETA_DIST = ./beta_dist
GPG_ID = CA0B97334F9449EB5AFFCB93240BD54D194E3161

########################################################################################################################
# `make help` Needs to be first so it is ran when just `make` is called
########################################################################################################################


.PHONY: help
help: # Show this help screen
	@ack '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) |\
	sort -k1,1 |\
	awk 'BEGIN {FS = ":.*?# "}; {printf "\033[1m%-30s\033[0m %s\n", $$1, $$2}'


########################################################################################################################
# Project Publishing
########################################################################################################################


.PHONY: test-publish
test-publish: build-beta # Publish to testpypi
	twine upload --repository testpypi --sign --identity $(GPG_ID) $(BETA_DIST)/*


########################################################################################################################
# Project Building
########################################################################################################################

.PHONY: build-beta
build-beta: build-pre build-beta-package # Build the beta package

#---------------------------------------------------------------------------------------------------
# Beta Build Subcommands (Test PyPi)
#---------------------------------------------------------------------------------------------------

# Build 'sdist' and 'bdist_wheel' for the beta package
.PHONY: build-beta-package
build-beta-package:
	./scripts/version_manager.py set-beta-build && \
	./scripts/version_manager.py check && \
	python setup.py sdist --dist-dir $(BETA_DIST) bdist_wheel --dist-dir $(BETA_DIST) && \
	./scripts/version_manager.py unset-beta-build && \
	:

########################################################################################################################
# Unsorted Targets
########################################################################################################################

.PHONY: build
build: build-pre build-package # Build the release package


.PHONY: build-package
build-package: # Build 'sdist' and 'bdist_wheel' for this package
	python setup.py sdist bdist_wheel


.PHONY: build-pre
build-pre: clean version-check test # Perform required pre-build steps


.PHONY: clean
clean: # Clean up build, test, and other project artifacts
	rm -rf \
	./.cache \
	./*.egg-info \
	$(BETA_DIST) \
	./build \
	./htmlcov \
	.coverage \
	coverage.xml \
	&& \
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf \
	&& :


.PHONY: publish
publish: build # Build, sign, and publish the package
	twine upload dist/* --sign -r pypi


.PHONY: test
test: test-flake test-unit # Run the full testing suite


.PHONY: test-flake
test-flake: # Run flake8 against project files
	flake8 -v


.PHONY: test-unit
test-unit: # Run only unit tests
	coverage run \
	--source="./letsencrypt" \
	--omit="\
	./letsencrypt/migrations/*,\
	./letsencrypt/admin.py,\
	./letsencrypt/apps.py,\
	./letsencrypt/tests.py,\
	./letsencrypt/urls.py,\
	" \
	example_project/manage.py test \
	--settings=example_project.settings_test \
	&& coverage report


.PHONY: version-check
version-check: # Verify the project version string is correct across the project
	./scripts/version_manager.py check
