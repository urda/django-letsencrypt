#!/usr/bin/env python
"""
Copyright 2017 Peter Urda

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

import os
import sys

import django


if __name__ == '__main__':
    # Configure Django before importing models
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_project.settings")
    django.setup()

    # Import required models for this script
    from django.contrib.auth.models import User

    username = 'admin'
    password = 'admin123'

    if not User.objects.filter(username=username).first():
        new_user = User.objects.create_superuser(
            username=username,
            email='admin@example.com',
            password=password,
        )
        new_user.first_name = 'Admin'
        new_user.last_name = 'User'

        new_user.save()

        print(
            "Created superuser '{username}' with password '{password}'".format(
                username=username,
                password=password,
            )
        )
    else:
        print("User '{}' already exists, doing nothing.".format(username))

    sys.exit(0)
