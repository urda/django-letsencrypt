.PHONY: test
test: test-flake test-unit

.PHONY: test-flake
test-flake:
	flake8 -v

.PHONY: test-unit
test-unit:
	coverage run \
	--source="./letsencrypt" \
	--omit="\
	./letsencrypt/admin.py,\
	./letsencrypt/tests.py,\
	./letsencrypt/urls.py,\
	./letsencrypt/views.py\
	" \
	runtests.py \
	&& coverage report
