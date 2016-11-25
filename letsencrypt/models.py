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

from django.core.urlresolvers import (
    reverse,
    NoReverseMatch,
)
from django.db import models


class AcmeChallenge(models.Model):
    """
    Simple model to handle Let's Encrypt .well-known/acme-challenge objects
    """

    challenge = models.TextField(
        help_text='The identifier for this challenge',
        unique=True,
    )

    response = models.TextField(
        help_text='The response expected for this challenge',
    )

    created_ts = models.DateTimeField(
        "Created Timestamp",
        auto_now_add=True,
    )

    updated_ts = models.DateTimeField(
        "Updated Timestamp",
        auto_now=True,
    )

    def __str__(self):
        return self.challenge

    def get_acme_url(self):
        """
        Get the URL to this ACME challenge
        :return: The URL as a string
        """
        try:
            return reverse(
                viewname='detail',
                current_app='letsencrypt',
                args=[self.challenge],
            )
        except NoReverseMatch:
            return ''

    class Meta:
        verbose_name = 'ACME Challenge'
        verbose_name_plural = 'ACME Challenges'
