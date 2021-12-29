#!/usr/bin/env python3

"""
Copyright 2020-2021 Peter Urda

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

import urllib.parse
import urllib.request
import urllib.response

import pytest


def build_url_for_challenge(base_url: str, challenge: str) -> str:
    return urllib.parse.urljoin(base_url, challenge)


def get_base_url() -> str:
    return 'http://localhost:8000/.well-known/acme-challenge/'


@pytest.mark.parametrize("expected_challenge,expected_response", [
    ('sample_challenge_00', 'sample_challenge_00_response'),
    ('sample_challenge_01', 'sample_challenge_01_response'),
    ('sample_challenge_02', 'sample_challenge_02_response'),
])
def test_responses(expected_challenge, expected_response):
    target_url = build_url_for_challenge(get_base_url(), expected_challenge)

    with urllib.request.urlopen(target_url) as url_response:
        actual_response = url_response.read().decode('utf-8')
        assert expected_response == actual_response
