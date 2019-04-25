from ynab_sdk_python.api.models.budget_detail import BudgetDetailResponse
from ynab_sdk_python.api.models.budget_settings import BudgetSettingsResponse
from ynab_sdk_python.api.models.budget_summary import BudgetSummaryResponse
from ynab_sdk_python.utils.api_client import ApiClient


class BudgetsApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def get_budgets(self) -> BudgetSummaryResponse:
        response = self.client.get('/budgets')
        return BudgetSummaryResponse.from_dict(response)

    def get_budget(self, budget_id: str) -> BudgetDetailResponse:
        response = self.client.get(f'/budgets/{budget_id}')
        return BudgetDetailResponse.from_dict(response)

    def get_budget_settings(self, budget_id: str) -> BudgetSettingsResponse:
        return self.client.get(f'/budgets/{budget_id}/settings')
