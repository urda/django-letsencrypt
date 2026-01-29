# `django-letsencrypt` Example Project

This is a simple `Django` example project that demonstrates the functionality
and usage of the `django-letsencrypt` project. It uses a local `db.sqlite3`
database, and a `Makefile` is provided to help you quickly set up the project
and take a look around.

## Setting up and Running the Example Project

1. From the repo root, run `uv sync` to create the virtual environment and install dependencies.
2. `cd` into **this** directory.
  - `(git project root)/example_project`
3. `make setup-project`
4. `make run-project`
5. You can now visit `http://127.0.0.1:8000/` to work with `django-letsencrypt`
  - Default admin login is:
    - Username: `admin`
    - Password: `admin123`

## Resetting the Example Project

1. `Ctrl-c` out of `make run-project` (or just stop the server if running in
   another fashion).
2. `rm db.sqlite3`
3. From the repo root, run `uv sync` if you have not already, then run
   `make setup-project` to start with a clean database again. Repeat the other
   directions to login to the example project as before.
