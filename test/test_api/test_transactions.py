import dataclasses
import test.support.fixtures.transactions as transaction_fixtures
from test.support.dummy_client import DummyClient
from test.support.mock import build_get_mock, build_post_mock, build_put_mock
from unittest import TestCase

from kgb import SpyAgency

from ynab_sdk import YNAB
from ynab_sdk.api.models.requests.transaction import TransactionRequest
from ynab_sdk.api.models.responses.transactions import TransactionsResponse


class TransactionsTest(SpyAgency, TestCase):
    ynab: YNAB
    client: DummyClient

    def setUp(self):
        self.client = DummyClient()
        self.ynab = YNAB(client=self.client)

    def test_get_transactions_with_success(self):
        spy = self.spy_on(
            self.client.get,
            call_fake=build_get_mock(transaction_fixtures.VALID_TRANSACTIONS),
        )
        transactions = self.ynab.transactions.get_transactions("some-budget")

        self.assertTrue(spy.called_with("/budgets/some-budget/transactions"))
        self.assertIsNotNone(transactions)
        self.assertIsInstance(transactions, TransactionsResponse)

    def test_get_transactions_from_account_with_success(self):
        spy = self.spy_on(
            self.client.get,
            call_fake=build_get_mock(transaction_fixtures.VALID_TRANSACTIONS),
        )
        transactions = self.ynab.transactions.get_transactions_from_account(
            "some-budget", "some-account"
        )

        self.assertTrue(
            spy.called_with("/budgets/some-budget/accounts/some-account/transactions")
        )
        self.assertIsNotNone(transactions)
        self.assertIsInstance(transactions, TransactionsResponse)

    def test_create_transactions_with_success(self):
        spy = self.spy_on(self.client.post, call_fake=build_post_mock())
        transactions = [TransactionRequest("some-account", "some-date", 123123)]
        response = self.ynab.transactions.create_transactions(
            "some-budget", transactions
        )

        payload = {"transactions": [dataclasses.asdict(t) for t in transactions]}

        self.assertTrue(spy.called_with("/budgets/some-budget/transactions", payload))
        self.assertIsNotNone(response)

    def test_update_transaction_with_success(self):
        spy = self.spy_on(self.client.put, call_fake=build_put_mock())
        transaction = TransactionRequest("some-account", "some-date", 123123)
        response = self.ynab.transactions.update_transaction(
            "some-budget", "some-transaction", transaction
        )

        payload = {"transaction": dataclasses.asdict(transaction)}

        self.assertTrue(
            spy.called_with(
                "/budgets/some-budget/transactions/some-transaction", payload
            )
        )
        self.assertIsNotNone(response)
