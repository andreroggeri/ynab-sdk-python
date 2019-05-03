from unittest import TestCase

from kgb import SpyAgency

from test.support.dummy_client import DummyClient
import test.support.fixtures.accounts as account_fixtures
from ynab_sdk_python import YNAB


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
        accounts = self.ynab.accounts.get_accounts('some-budget')

        self.assertTrue(spy.called_with('/budgets/some-budget/accounts'))
        self.assertIsNotNone(accounts)

    def test_get_account_with_success(self):
        spy = self.spy_on(self.client.get, call_fake=mock_valid_account)
        account = self.ynab.accounts.get_account('some-budget', 'some-account')

        self.assertTrue(spy.called_with('/budgets/some-budget/accounts/some-account'))
        self.assertIsNotNone(account)
