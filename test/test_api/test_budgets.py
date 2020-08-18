import test.support.fixtures.budgets as budget_fixtures
from test.support.dummy_client import DummyClient
from test.support.mock import build_get_mock
from unittest import TestCase

from kgb import SpyAgency

from ynab_sdk import YNAB
from ynab_sdk.api.models.responses.budget_detail import BudgetDetailResponse
from ynab_sdk.api.models.responses.budget_settings import BudgetSettingsResponse
from ynab_sdk.api.models.responses.budget_summary import BudgetSummaryResponse


class BudgetsTest(SpyAgency, TestCase):
    ynab: YNAB
    client: DummyClient

    def setUp(self):
        self.client = DummyClient()
        self.ynab = YNAB(client=self.client)

    def test_get_budgets_with_success(self):
        spy = self.spy_on(
            self.client.get, call_fake=build_get_mock(budget_fixtures.VALID_BUDGETS)
        )
        budgets = self.ynab.budgets.get_budgets()

        self.assertTrue(spy.called_with("/budgets"))
        self.assertIsNotNone(budgets)
        self.assertIsInstance(budgets, BudgetSummaryResponse)

    def test_get_budget_with_success(self):
        spy = self.spy_on(
            self.client.get, call_fake=build_get_mock(budget_fixtures.VALID_BUDGET)
        )
        budget = self.ynab.budgets.get_budget("abc-123")

        self.assertTrue(spy.called_with("/budgets/abc-123"))
        self.assertIsNotNone(budget)
        self.assertIsInstance(budget, BudgetDetailResponse)

    def test_get_budget_settings_with_success(self):
        spy = self.spy_on(
            self.client.get, call_fake=build_get_mock(budget_fixtures.VALID_SETTINGS)
        )
        settings = self.ynab.budgets.get_budget_settings("abc-123")

        self.assertTrue(spy.called_with("/budgets/abc-123/settings"))
        self.assertIsNotNone(settings)
        self.assertIsInstance(settings, BudgetSettingsResponse)
