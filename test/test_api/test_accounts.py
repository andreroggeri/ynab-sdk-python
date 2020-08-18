import test.support.fixtures.accounts as account_fixtures
from test.support.dummy_client import DummyClient
from unittest import TestCase

from kgb import SpyAgency

from ynab_sdk import YNAB
from ynab_sdk.api.models.responses.account import AccountResponse
from ynab_sdk.api.models.responses.accounts import AccountsResponse


def mock_valid_accounts(self, endpoint):
    return account_fixtures.VALID_ACCOUNTS


def mock_valid_account(self, endpoint):
    return account_fixtures.VALID_ACCOUNT


class AccountsTest(SpyAgency, TestCase):
    ynab: YNAB
    client: DummyClient

    def setUp(self):
        self.client = DummyClient()
        self.ynab = YNAB(client=self.client)

    def test_get_accounts_with_success(self):
        spy = self.spy_on(self.client.get, call_fake=mock_valid_accounts)
        accounts = self.ynab.accounts.get_accounts("some-budget")

        self.assertTrue(spy.called_with("/budgets/some-budget/accounts"))
        self.assertIsNotNone(accounts)
        self.assertIsInstance(accounts, AccountsResponse)

    def test_get_account_with_success(self):
        spy = self.spy_on(self.client.get, call_fake=mock_valid_account)
        account = self.ynab.accounts.get_account("some-budget", "some-account")

        self.assertTrue(spy.called_with("/budgets/some-budget/accounts/some-account"))
        self.assertIsNotNone(account)
        self.assertIsInstance(account, AccountResponse)
