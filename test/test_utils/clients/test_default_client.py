from unittest import TestCase
from unittest.mock import Mock

import requests
from kgb import SpyAgency
from requests import Response

from ynab_sdk.utils.clients.default_client import DefaultClient
from ynab_sdk.utils.configurations.default import DefaultConfig


def fake_get(url, **kwargs):
    response = Mock(spec=Response)
    response.json.return_value = {}
    return response


def fake_post(url, data=None, json=None, **kwargs):
    response = Mock(spec=Response)
    response.json.return_value = {}
    return response


class DefaultClientTest(SpyAgency, TestCase):
    config: DefaultConfig
    client: DefaultClient

    def setUp(self):
        self.config = DefaultConfig("some-key")
        self.client = DefaultClient(self.config)

    def test_succesful_get(self):
        spy = self.spy_on(requests.get, call_fake=fake_get)

        self.client.get("/some-endpoint")

        expected_endpoint = self.config.full_url + "/some-endpoint"
        self.assertTrue(spy.called_with(expected_endpoint, headers=self.client.headers))

    def test_succesful_post(self):
        spy = self.spy_on(requests.post, call_fake=fake_post)
        payload = {"key": "value"}
        self.client.post("/some-endpoint", payload)
