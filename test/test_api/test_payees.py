import test.support.fixtures.payees as payee_fixtures
from test.support.dummy_client import DummyClient
from test.support.mock import build_get_mock
from unittest import TestCase

from kgb import SpyAgency

from ynab_sdk import YNAB
from ynab_sdk.api.models.responses.payee import PayeeResponse
from ynab_sdk.api.models.responses.payees import PayeesResponse


class PayeesTest(SpyAgency, TestCase):
    ynab: YNAB
    client: DummyClient

    def setUp(self):
        self.client = DummyClient()
        self.ynab = YNAB(client=self.client)

    def test_get_payees_with_success(self):
        spy = self.spy_on(
            self.client.get, call_fake=build_get_mock(payee_fixtures.VALID_PAYEES)
        )
        payees = self.ynab.payees.get_payees("some-budget")

        self.assertTrue(spy.called_with("/budgets/some-budget/payees"))
        self.assertIsNotNone(payees)
        self.assertIsInstance(payees, PayeesResponse)

    def test_get_payee_with_success(self):
        spy = self.spy_on(
            self.client.get, call_fake=build_get_mock(payee_fixtures.VALID_PAYEE)
        )
        payee = self.ynab.payees.get_payee("some-budget", "some-payee")

        self.assertTrue(spy.called_with("/budgets/some-budget/payees/some-payee"))
        self.assertIsNotNone(payee)
        self.assertIsInstance(payee, PayeeResponse)
