.PHONY: test
test: version-check test-flake test-unit

.PHONY: test-flake
test-flake:
	flake8 -v

.PHONY: test-unit
test-unit:
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
