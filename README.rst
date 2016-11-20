Let's Encrypt App for Django
============================

This Django app makes it easy to manage all of your
`ACME challenges <https://letsencrypt.github.io/acme-spec/>`_.
:code:`django-letsencrypt` will add a simple model that you can manage through
the :code:`django` admin interface. Simply add your :code:`ACME challenge` and
:code:`response`, and your app will serve up the necessary URL for
`Let\'s Encrypt <https://letsencrypt.org/how-it-works/>`_ validation.

Quick Start
-----------

1. Add :code:`letsencrypt` to your :code:`INSTALLED_APPS`

.. code:: python

    INSTALLED_APPS = [
        ... ,
        'letsencrypt',
        ... ,
    ]

2. Included the :code:`letsencrypt` in your project's :code:`urls.py`,
   or where applicable

.. code:: python

    url(r'^.well-known/', include('letsencrypt.urls'))

3. Run :code:`manage.py migrate` to create the required table for the
   :code:`letsencrypt` model

4. Create your :code:`ACME Challenge` objects in your Django admin interface

5. Test your :code:`ACME Challenge` objects and their responses by visiting
   them:

    {Django Site}/.well-known/acme-challenge/challenge_text
