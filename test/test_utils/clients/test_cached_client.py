import json
from unittest import TestCase
from unittest.mock import MagicMock, Mock, PropertyMock

import requests
from kgb import SpyAgency
from redis import Redis
from requests import Response

from ynab_sdk.utils.clients.cached_client import CachedClient
from ynab_sdk.utils.configurations.cached import CachedConfig


def fake_get(url, **kwargs):
    response = MagicMock()
    type(response).status_code = PropertyMock(return_value=200)
    response.json.return_value = {}
    return response


def fake_get_error(url, **kwargs):
    response = MagicMock()
    type(response).status_code = PropertyMock(return_value=400)
    response.json.return_value = {}
    return response


def fake_post(url, data=None, json=None, **kwargs):
    response = Mock(spec=Response)
    type(response).status_code = PropertyMock(return_value=200)
    response.json.return_value = {}
    return response


def fake_redis_set(self, name, value, ex=None, px=None, nx=False, xx=False):
    return


def fake_redis_get(self, key):
    return None


class CachedClientTest(SpyAgency, TestCase):
    config: CachedConfig
    client: CachedClient

    def setUp(self):
        self.config = CachedConfig("redis", 6379, api_key="some-key")
        self.client = CachedClient(self.config)
        self.spy_on(Redis.__init__, call_original=False)

    def test_succesful_uncached_get(self):
        request_get_spy = self.spy_on(requests.get, call_fake=fake_get)
        self.spy_on(Redis.get, call_fake=fake_redis_get)
        self.spy_on(Redis.set, call_fake=fake_redis_set)

        self.client.get("/some-endpoint")

        expected_endpoint = self.config.full_url + "/some-endpoint"
        self.assertTrue(
            request_get_spy.called_with(expected_endpoint, headers=self.client.headers)
        )

    def test_succesful_cached_get(self):
        def fake_redis_get(self, key):
            return json.dumps({"some": "obj"})

        request_get_spy = self.spy_on(requests.get, call_fake=fake_get)
        self.spy_on(Redis.get, call_fake=fake_redis_get)

        self.client.get("/some-endpoint")

        self.assertFalse(request_get_spy.called)

    def test_unsucessful_get_should_not_cache(self):
        request_get_spy = self.spy_on(requests.get, call_fake=fake_get_error)
        redis_set_spy = self.spy_on(Redis.set, call_fake=fake_redis_set)
        self.spy_on(Redis.get, call_fake=fake_redis_get)

        self.client.get("/some-endpoint")

        expected_endpoint = self.config.full_url + "/some-endpoint"
        self.assertTrue(
            request_get_spy.called_with(expected_endpoint, headers=self.client.headers)
        )
        self.assertFalse(redis_set_spy.called)

    def test_succesful_post(self):
        spy = self.spy_on(requests.post, call_fake=fake_post)
        payload = {"key": "value"}
        self.client.post("/some-endpoint", payload)
