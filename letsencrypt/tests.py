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

from django.test import TestCase

from letsencrypt.models import AcmeChallenge


class TestAcmeChallenge(TestCase):
    """Test the ACME Challenge model for Let's Encrypt"""

    def test_acme_url(self):
        """Test the django reverse() lookup for the ACME url"""
        challenge = 'challenge-text-here'
        response = ''
        expected = '/acme-challenge/{}'.format(challenge)
        acme_object = AcmeChallenge(
            challenge=challenge,
            response=response,
        )

        self.assertEqual(
            acme_object.get_acme_url(),
            expected,
        )

    def test_acme_url_no_reverse_match(self):
        """Test an empty string for URL is returned on NoReverseMatch"""
        acme_object = AcmeChallenge()

        self.assertEqual(
            acme_object.get_acme_url(),
            '',
        )

    def test_challenge(self):
        """Test the challenge data in the model"""
        challenge = 'challenge'
        response = ''
        acme_object = AcmeChallenge(
            challenge=challenge,
            response=response,
        )

        self.assertEqual(
            acme_object.challenge,
            challenge,
        )

    def test_response(self):
        """Test the response data in the model"""

        challenge = ''
        response = 'challenge.response'
        acme_object = AcmeChallenge(
            challenge=challenge,
            response=response,
        )

        self.assertEqual(
            acme_object.response,
            response,
        )

    def test_str(self):
        """Test the __str__ representation"""

        challenge = 'challenge'
        response = 'challenge.response'
        acme_object = AcmeChallenge(
            challenge=challenge,
            response=response,
        )

        self.assertEqual(
            str(acme_object),
            challenge,
        )
