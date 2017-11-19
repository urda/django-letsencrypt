.PHONY: help
help: # Show this help screen
	@ack '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) |\
	sort -k1,1 |\
	awk 'BEGIN {FS = ":.*?# "}; {printf "\033[1m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: build
build: clean test build-package # Clean, Test, and Build the package


.PHONY: build-package
build-package: # Build 'sdist' and 'bdist_wheel' for this package
	python setup.py sdist bdist_wheel


.PHONY: clean
clean: # Clean up build, test, and other project artifacts
	rm -rf \
	./.cache \
	./*.egg-info \
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
