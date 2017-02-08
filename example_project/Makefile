.PHONY: help
help: # Show this help screen
	@ack '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) |\
	sort |\
	awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: create-example-data
create-example-data: # Create a few example ACME challenges
	./create_example_data.py


.PHONY: createsuperuser
createsuperuser: # Configure the default admin for the example project
	./create_superuser.py


.PHONY: migrate
migrate: # Run Django migrations on the example project
	python manage.py migrate


.PHONY: run-project
run-project: # Django runserver for the example project
	python manage.py runserver


.PHONY: setup-project
setup-project: migrate createsuperuser create-example-data # Configure the example project (migrate, create super user)
