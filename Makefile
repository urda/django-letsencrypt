########################################################################################################################
# Variables
########################################################################################################################

DIST = ./dist
BETA_DIST = ./beta_dist

#---------------------------------------------------------------------------------------------------
# Composite Variables
#---------------------------------------------------------------------------------------------------

CLEAN_TARGETS = ./.cache ./.tox ./*.egg-info ./.pytest_cache $(BETA_DIST) $(DIST) ./build ./htmlcov .coverage coverage.xml junit.xml junit-integration.xml

########################################################################################################################
# Utilities
########################################################################################################################

# `help` Needs to be first so it is ran when just `make` is called
.PHONY: help
help: # Show this help screen
	@ack '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) |\
	LC_ALL=C sort -t: -k1,1 |\
	awk 'BEGIN {FS = ":.*?# "}; {printf "\033[1m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: # Clean up build, test, and other project artifacts
	rm -rf $(CLEAN_TARGETS) && \
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf && \
	:

#---------------------------------------------------------------------------------------------------
# Versioning
#---------------------------------------------------------------------------------------------------

.PHONY: version-check
version-check: # Verify the project version string is correct across the project
	@uv run ./scripts/version_manager.py check

.PHONY: version-check-django
version-check-django: # Verify the project's Django version
	@uv run python -c 'import django; print(django.VERSION)'

########################################################################################################################
# Testing
########################################################################################################################

.PHONY: test
test: version-check test-flake test-unit test-coverage-report # Run the full testing suite

.PHONY: test-tox
test-tox: # Run tox for the project
	@uv run tox -p auto

#---------------------------------------------------------------------------------------------------
# Internal Test Commands
#---------------------------------------------------------------------------------------------------

# Report test coverage after tests are complete
.PHONY: test-coverage-report
test-coverage-report:
	@uv run coverage report

# Run flake8 against project files
.PHONY: test-flake
test-flake:
	@uv run flake8 -v

# Tox testing requires coverage to "append" results
.PHONY: test-tox-entry
test-tox-entry: COV-ARGS = --append
test-tox-entry: test-unit

# Run only unit tests
.PHONY: test-unit
test-unit:
	@uv run pytest letsencrypt/tests.py \
	--cov=letsencrypt \
	--cov-config=pyproject.toml \
	--cov-report=term-missing \
	--cov-report=xml \
	--junitxml=junit.xml \
	${PYTEST-ARGS} \

########################################################################################################################
# Integration Testing
########################################################################################################################

.PHONY: test-integration
test-integration: # Run the integration tests for the project
	@./scripts/local_integration.sh

.PHONY: test-integration-testpypi
test-integration-testpypi: # Test the deployed Test PyPI package (requires VERSION arg)
	@./scripts/testpypi_integration.sh $(VERSION)

.PHONY: test-integration-testpypi-tox
test-integration-testpypi-tox: # Test the deployed Test PyPI package for all versions in parallel with tox (requires VERSION arg)
	@TESTPYPI_VERSION=$(VERSION) uv run tox -m testpypi -p all

########################################################################################################################
# Building
########################################################################################################################

.PHONY: build
build: build-pre build-package # Build the release package

.PHONY: build-beta
build-beta: build-pre build-beta-package # Build the beta package

#---------------------------------------------------------------------------------------------------
# Internal Build Commands
#---------------------------------------------------------------------------------------------------

# Perform required pre-build steps for all build types
.PHONY: build-pre
build-pre: version-check clean test

# Build 'sdist' and 'bdist_wheel' for this package (PyPI)
.PHONY: build-package
build-package:
	uv build --out-dir $(DIST)

# Build 'sdist' and 'bdist_wheel' for the beta package (Test PyPI)
.PHONY: build-beta-package
build-beta-package:
	uv run ./scripts/version_manager.py set-beta-build && \
	uv run ./scripts/version_manager.py check && \
	uv build --out-dir $(BETA_DIST) && \
	uv run ./scripts/version_manager.py unset-beta-build && \
	:

########################################################################################################################
# Publishing
########################################################################################################################

.PHONY: publish
publish: build # Build and publish the package to PyPI
	uv run twine upload --repository pypi $(DIST)/*

.PHONY: publish-test
publish-test: build-beta # Build and publish the package to Test PyPI
	uv run twine upload --repository testpypi $(BETA_DIST)/*
