########################################################################################################################
# Variables
########################################################################################################################

BETA_DIST = ./beta_dist
CLEAN_TARGETS = ./.cache ./*.egg-info $(BETA_DIST) $(DIST) ./build ./htmlcov .coverage coverage.xml
DIST = ./dist
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
# Testing
########################################################################################################################


.PHONY: test
test: version-check test-flake test-unit test-coverage-report # Run the full testing suite


.PHONY: version-check
version-check: # Verify the project version string is correct across the project
	./scripts/version_manager.py check


#---------------------------------------------------------------------------------------------------
# Test Subcommands
#---------------------------------------------------------------------------------------------------


# Report test coverage after tests are complete
.PHONY: test-coverage-report
test-coverage-report:
	coverage report


# Run flake8 against project files
.PHONY: test-flake
test-flake:
	flake8 -v


# Tox testing requires coverage to "append" results
.PHONY: test-tox
test-tox: COV-ARGS = --append
test-tox: test-unit


# Run only unit tests
.PHONY: test-unit
test-unit:
	coverage run \
	${COV-ARGS} \
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


########################################################################################################################
# Integration Testing
########################################################################################################################


.PHONY: test-integration
test-integration: # Run the integration tests for the project
	./scripts/local_integration.sh


########################################################################################################################
# Project Publishing
########################################################################################################################


.PHONY: publish
publish: build # Build, sign, and publish the package to PyPi
	twine upload --repository pypi --sign --identity $(GPG_ID) $(DIST)/*


.PHONY: test-publish
test-publish: build-beta # Build, sign, and publish the package to TestPyPi
	twine upload --repository testpypi --sign --identity $(GPG_ID) $(BETA_DIST)/*


########################################################################################################################
# Project Building
########################################################################################################################


.PHONY: build
build: build-pre build-package # Build the release package


.PHONY: build-beta
build-beta: build-pre build-beta-package # Build the beta package


.PHONY: clean
clean: # Clean up build, test, and other project artifacts
	rm -rf $(CLEAN_TARGETS) && \
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf && \
	:

#---------------------------------------------------------------------------------------------------
# Build Subcommands
#---------------------------------------------------------------------------------------------------


# Perform required pre-build steps for all build types
.PHONY: build-pre
build-pre: version-check clean test


#---------------------------------------------------------------------------------------------------
# Build Subcommands (PyPi)
#---------------------------------------------------------------------------------------------------


# Build 'sdist' and 'bdist_wheel' for this package
.PHONY: build-package
build-package:
	python setup.py sdist --dist-dir $(DIST) bdist_wheel --dist-dir $(DIST)


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
