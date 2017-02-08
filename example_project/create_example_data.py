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
    from letsencrypt.models import AcmeChallenge

    sample_data_prefix = 'sample_challenge'
    sample_data_count = 3

    for x in range(sample_data_count):
        challenge = "{0}_{1:0>2}".format(sample_data_prefix, x)
        response = "{0}_response".format(challenge)

        if not AcmeChallenge.objects.filter(challenge=challenge).first():
            new_challenge = AcmeChallenge(
                challenge=challenge,
                response=response,
            )
            new_challenge.save()

            print("Created challenge '{}'".format(challenge))
        else:
            print("Challenge '{}' already exists".format(challenge))

    sys.exit(0)
