# Let's Encrypt App for Django

[![Travis Build Status (Master)](https://travis-ci.org/urda/django-letsencrypt.svg?branch=master)](https://travis-ci.org/urda/django-letsencrypt) [![Codecov Status (Master)](https://codecov.io/gh/urda/django-letsencrypt/branch/master/graph/badge.svg)](https://codecov.io/gh/urda/django-letsencrypt/branch/master)

`django-letsencrypt` will allow you to add, remove, and update any
[ACME challenge](https://github.com/ietf-wg-acme/acme/) objects you may
need through your Django admin interface. Simply add the `ACME challenge`
and `response` for your app to serve up the necessary information for
[Let's Encrypt](https://letsencrypt.org/how-it-works/) validation.

## Installation & Configuration

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
