Let's Encrypt App for Django
============================

.. image:: https://travis-ci.org/urda/django-letsencrypt.svg?branch=master
   :target: https://travis-ci.org/urda/django-letsencrypt

.. image:: https://codecov.io/gh/urda/django-letsencrypt/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/urda/django-letsencrypt/branch/master

:code:`django-letsencrypt` will allow you to add, remove, and update any
`ACME challenge <https://letsencrypt.github.io/acme-spec/>`_ objects you may
need through your Django admin interface. Simply add the :code:`ACME challenge`
and :code:`response` for your app to serve up the necessary information for
`Let\'s Encrypt <https://letsencrypt.org/how-it-works/>`_ validation.

Installation & Configuration
----------------------------

#. :code:`pip install django-letsencrypt`

#. Add :code:`letsencrypt` to your :code:`INSTALLED_APPS`

   .. code:: python

       INSTALLED_APPS = [
           ... ,
           'letsencrypt',
           ... ,
       ]

#. Include the :code:`letsencrypt` in your project's :code:`urls.py`,
   or where applicable (usually your root :code:`urls.py`).

   .. code:: python

       url(r'^\.well-known/', include('letsencrypt.urls'))

#. Run :code:`manage.py migrate` to create the required table for the
   :code:`letsencrypt` model

#. Create your :code:`ACME Challenge` objects in your Django admin interface

#. Test your :code:`ACME Challenge` objects and their responses by visiting
   them:

   .. code::

       {Django Site}/.well-known/acme-challenge/challenge_text

#. Enjoy your easy to manage `ACME Challenges` inside your Django project!
