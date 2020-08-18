from ynab_sdk.api.models.responses.categories import CategoriesResponse
from ynab_sdk.api.models.responses.category import CategoryResponse
from ynab_sdk.utils.clients.base_client import BaseClient


class CategoriesApi:
    def __init__(self, client: BaseClient):
        self.client = client

    def get_categories(self, budget_id: str) -> CategoriesResponse:
        response = self.client.get(f"/budgets/{budget_id}/categories")
        return CategoriesResponse.from_dict(response)

    def get_category(self, budget_id: str, category_id: str) -> CategoryResponse:
        response = self.client.get(f"/budgets/{budget_id}/categories/{category_id}")
        return CategoryResponse.from_dict(response)
