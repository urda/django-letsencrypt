"""
Copyright 2017-2021 Peter Urda

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

from .settings import *  # noqa


DATABASE_ENGINE = os.getenv('DATABASE_ENGINE', default='sqlite')  # noqa

TEST_DATABASES = {
    'mysql': {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'gh_actions_test',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        },
    },

    'postgres': {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gh_actions_test',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        },
    },

    'sqlite': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        },
    },
}

DATABASES = TEST_DATABASES.get(DATABASE_ENGINE, TEST_DATABASES['sqlite'])
