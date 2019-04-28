from unittest import TestCase

from test.support.dummy_client import DummyClient
from ynab_sdk_python import YNAB


class YNABTest(TestCase):
    ynab: YNAB
    client: DummyClient

    def setUp(self):
        self.client = DummyClient()
        self.ynab = YNAB(client=self.client)

    def test_client_requires_key_or_client(self):
        self.assertRaises(AssertionError, YNAB)
