#!/usr/bin/env python

"""
Copyright 2016 Peter Urda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner


settings.configure(
    DATABASES={
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
      }
    },
    DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'letsencrypt',
    ),
    ROOT_URLCONF='letsencrypt.urls',
)


if __name__ == '__main__':
    django.setup()
    test_runner = DiscoverRunner(verbosity=1)
    failures = test_runner.run_tests(['letsencrypt'])

    if failures:
        sys.exit(failures)
