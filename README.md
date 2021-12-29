# Let's Encrypt App for Django

`django-letsencrypt` will allow you to add, remove, and update any
[ACME challenge](https://github.com/ietf-wg-acme/acme/) objects you may
need through your Django admin interface. Simply add the `ACME challenge`
and `response` for your app to serve up the necessary information for
[Let's Encrypt](https://letsencrypt.org/how-it-works/) validation.

This project strives to make installation, configuration, and usage a snap!
From high levels of code coverage, multiple compatible python versions, multiple
versions of Django supported, even multiple databases too!

And of course all wrapped up and published to
[PyPI](https://pypi.org/project/django-letsencrypt/) for standard installation!

# Supported Configurations

`django-letsencrypt` is tested across a number of configurations, here's what's
supported so far:

- Python Versions Supported:
  - `3.10` (Django `4.0` and `3.2` only)
  - `3.8`
  - `3.7` (Django `3.2` and `2.2` only)
- Django Versions Supported:
  - `4.0` minimum version `4.0`
  - `3.2` minimum version `3.2.10`
  - `2.2` minimum version `2.2.25`
- Databases Supported:
  - `mysql`
  - `postgres`
  - `sqlite`

# Recent Build Status Badges

- [![Linting - Master](https://github.com/urda/django-letsencrypt/actions/workflows/linting.yaml/badge.svg?branch=master)](https://github.com/urda/django-letsencrypt/actions/workflows/linting.yaml)
- [![Testing Django 2.2 - Master](https://github.com/urda/django-letsencrypt/actions/workflows/testing-22.yaml/badge.svg?branch=master)](https://github.com/urda/django-letsencrypt/actions/workflows/testing-22.yaml)
- [![Testing Django 3.2 - Master](https://github.com/urda/django-letsencrypt/actions/workflows/testing-32.yaml/badge.svg?branch=master)](https://github.com/urda/django-letsencrypt/actions/workflows/testing-32.yaml)
- [![Testing Django 4.0 - Master](https://github.com/urda/django-letsencrypt/actions/workflows/testing-40.yaml/badge.svg?branch=master)](https://github.com/urda/django-letsencrypt/actions/workflows/testing-40.yaml)
- [![Codecov - Master](https://codecov.io/gh/urda/django-letsencrypt/branch/master/graph/badge.svg?token=yn64lBfwZr)](https://codecov.io/gh/urda/django-letsencrypt)

# Installation & Configuration

1. `pip install django-letsencrypt`

2. Add `letsencrypt` to your `INSTALLED_APPS`

```python
INSTALLED_APPS = [
   ... ,
   'letsencrypt',
   ... ,
]
```

3. Include the `letsencrypt` in your project's `urls.py`,
   or where applicable (usually your root `urls.py`).

```python
re_path(r'^\.well-known/', include('letsencrypt.urls'))
```

4. Run `manage.py migrate` to create the required table for the
   `letsencrypt` model

5. Create your `ACME Challenge` objects in your Django admin interface

6. Test your `ACME Challenge` objects and their responses by visiting
   them:

```
{Django Site}/.well-known/acme-challenge/challenge_text
```

7. Enjoy your easy to manage `ACME Challenges` inside your Django project!

# Example Project

If you would like a demo of how to use this application simply clone this project's
`git` repository from [GitHub](https://github.com/urda/django-letsencrypt),
take a moment to read the `README.md` file within the
[`example_project`](https://github.com/urda/django-letsencrypt/tree/master/example_project)
directory, and follow the directions. That will spin up a small sample django
application already configured for you to try out.
