# `django-letsencrypt` Example Project

This is a simple `Django` example project that demonstrates the funcionality
and usage of the `django-letsencrypt` project. It uses a local `db.sqlite3`
database, and a `Makefile` is provided to help you quickly up the project
and take a look around.

## Setting up and Running the Example Project

1. `cd` into **this** directory.
  - `(git project root)/example_project`
2. `mkvirtualenv django-le-example -p $(which python3)`
  - `mkvirtualenv` should immediately start using this `virtualenv`. If not,
    make sure you `workon` it first.
3. `pip install -r requirements.txt`
4. `make setup-project`
5. `make run-project`
6. You can now visit `http://127.0.0.1:8000/` to work with `django-letsencrypt`
  - Default admin login is:
    - Username: `admin`
    - Password: `admin123`

## Resetting the Example Project

1. `Ctrl-c` out of `make run-project` (or just stop the server if running in
   another fashion).
2. `rm db.sqlite3`
3. Make sure you are inside your `virtualenv`, and simply run
   `make setup-project` to start with a clean database again. Repeat the other
   directions to login to the example project as before.
