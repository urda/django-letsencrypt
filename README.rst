Let's Encrypt App for Django
============================

Quick Start
-----------

1. Add :code:`letsencrypt` to your :code:`INSTALLED_APPS`

.. code:: python

    INSTALLED_APPS = [
        ... ,
        'letsencrypt',
        ... ,
    ]

2. Included the :code:`letsencrypt` in your project's :code:`urls.py`, or where applicable

.. code:: python

    url(r'^.well-known/', include('letsencrypt.urls'))

3. Run :code:`manage.py migrate` to create the required tables for the :code:`letsencrypt` models

4. Create your :code:`ACME Challenge` objects in your Django admin interface

5. Test your :code:`ACME Challenge` objects and their responses by visiting them:

    {Django Site}/.well-known/acme-challenge/challenge_text
