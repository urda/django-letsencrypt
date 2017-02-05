.PHONY: help
help: # Show this help screen
	@ack '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) |\
	sort |\
	awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


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
	./letsencrypt/views.py\
	" \
	runtests.py \
	&& coverage report


.PHONY: version-check
version-check: # Verify the project version string is correct across the project
	./scripts/version_manager.py check
