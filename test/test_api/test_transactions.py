from unittest import TestCase

from kgb import SpyAgency

import test.support.fixtures.transactions as transaction_fixtures
from test.support.dummy_client import DummyClient
from test.support.mock import build_get_mock, build_post_mock
from ynab_sdk_python import YNAB


class TransactionsTest(SpyAgency, TestCase):
    ynab: YNAB
    client: DummyClient

    def setUp(self):
        self.client = DummyClient()
        self.ynab = YNAB(client=self.client)

    def test_get_transactions_with_success(self):
        spy = self.spy_on(self.client.get, call_fake=build_get_mock(transaction_fixtures.VALID_TRANSACTIONS))
        transactions = self.ynab.transactions.get_transactions('some-budget')

        self.assertTrue(spy.called_with('/budgets/some-budget/transactions'))
        self.assertIsNotNone(transactions)

    def test_create_transactions_with_success(self):
        spy = self.spy_on(self.client.post, call_fake=build_post_mock())
        transactions = self.ynab.transactions.create_transactions('some-budget', {})

        payload = {'transactions': {}}

        self.assertTrue(spy.called_with('/budgets/some-budget/transactions', payload))
        self.assertIsNotNone(transactions)
