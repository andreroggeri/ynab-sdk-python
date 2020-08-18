from test.support.dummy_client import DummyClient
from unittest import TestCase

from ynab_sdk import YNAB


class YNABTest(TestCase):
    ynab: YNAB
    client: DummyClient

    def setUp(self):
        self.client = DummyClient()
        self.ynab = YNAB(client=self.client)

    def test_client_requires_key_or_client(self):
        self.assertRaises(AssertionError, YNAB)
