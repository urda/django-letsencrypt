"""
Copyright 2016-2017 Peter Urda

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

from django.http import Http404
from django.test import (
    RequestFactory,
    TestCase,
)

from .models import AcmeChallenge
from .views import detail


class TestAcmeChallenge(TestCase):
    """Test the ACME Challenge model for Let's Encrypt"""

    def test_acme_url(self):
        """Test the django reverse() lookup for the ACME url"""
        challenge = 'challenge-text-here'
        response = ''
        expected = '/.well-known/acme-challenge/{}'.format(challenge)
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


class TestAcmeChallengeViews(TestCase):
    """Test the ACME Challenge views for the project"""

    def setUp(self):
        self.factory = RequestFactory()

        self.detail_url = '/.well-known/acme-challenge'

        self.expected_challenge = 'challenge_view_test'
        self.expected_response = 'challenge_view_test_response'
        self.expected_response_bytes = b'challenge_view_test_response'
        self.expected_response_decode = 'challenge_view_test_response'

        self.test_challenge = AcmeChallenge.objects.create(
            challenge=self.expected_challenge,
            response=self.expected_response,
        )

    def test_detail(self):
        """
        When given a valid request challenge,
        make sure the response is returned
        """
        request = self.factory.get(self.detail_url)

        response = detail(request, self.expected_challenge)

        # Check status of response
        self.assertEqual(response.reason_phrase, 'OK')
        self.assertEqual(response.status_code, 200)

        # Check content of response
        self.assertEqual(response.content, self.expected_response_bytes)
        self.assertEqual(
            response.content.decode(response.charset),
            self.expected_response_decode,
        )

    def test_detail_404(self):
        """When given a bad request challenge, make sure a 404 is returned"""
        request = self.factory.get(self.detail_url)

        with self.assertRaises(Http404):
            detail(request, 'fake')
