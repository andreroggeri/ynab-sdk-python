import test.support.fixtures.categories as categories_fixtures
from test.support.dummy_client import DummyClient
from test.support.mock import build_get_mock
from unittest import TestCase

from kgb import SpyAgency

from ynab_sdk import YNAB
from ynab_sdk.api.models.responses.categories import CategoriesResponse
from ynab_sdk.api.models.responses.category import CategoryResponse


class CategoriesTest(SpyAgency, TestCase):
    ynab: YNAB
    client: DummyClient

    def setUp(self):
        self.client = DummyClient()
        self.ynab = YNAB(client=self.client)

    def test_get_categories_with_success(self):
        spy = self.spy_on(
            self.client.get,
            call_fake=build_get_mock(categories_fixtures.VALID_CATEGORIES),
        )
        categories = self.ynab.categories.get_categories("some-budget")

        self.assertTrue(spy.called_with("/budgets/some-budget/categories"))
        self.assertIsNotNone(categories)
        self.assertIsInstance(categories, CategoriesResponse)

    def test_get_categoru_with_success(self):
        spy = self.spy_on(
            self.client.get,
            call_fake=build_get_mock(categories_fixtures.VALID_CATEGORY),
        )
        category = self.ynab.categories.get_category("some-budget", "some-category")

        self.assertTrue(
            spy.called_with("/budgets/some-budget/categories/some-category")
        )
        self.assertIsNotNone(category)
        self.assertIsInstance(category, CategoryResponse)
