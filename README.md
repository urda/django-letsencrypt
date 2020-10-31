# Let's Encrypt App for Django

[![Travis Build Status (Master)](https://travis-ci.com/urda/django-letsencrypt.svg?branch=master)](https://travis-ci.com/urda/django-letsencrypt) [![Codecov Status (Master)](https://codecov.io/gh/urda/django-letsencrypt/branch/master/graph/badge.svg)](https://codecov.io/gh/urda/django-letsencrypt/branch/master)

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
  - `3.8`
  - `3.7`
  - `3.6`
- Django Versions Supported:
  - `3.1` minimum version `3.1.2`
  - `3.0` minimum version `3.0.10`
  - `2.2` minimum version `2.2.16`
- Databases Supported:
  - `mysql`
  - `postgres`
  - `sqlite`

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
url(r'^\.well-known/', include('letsencrypt.urls'))
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
