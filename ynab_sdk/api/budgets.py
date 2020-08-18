from ynab_sdk.api.models.responses.budget_detail import BudgetDetailResponse
from ynab_sdk.api.models.responses.budget_settings import BudgetSettingsResponse
from ynab_sdk.api.models.responses.budget_summary import BudgetSummaryResponse
from ynab_sdk.utils.clients.base_client import BaseClient


class BudgetsApi:
    def __init__(self, client: BaseClient):
        self.client = client

    def get_budgets(self) -> BudgetSummaryResponse:
        response = self.client.get("/budgets")
        return BudgetSummaryResponse.from_dict(response)

    def get_budget(self, budget_id: str) -> BudgetDetailResponse:
        response = self.client.get(f"/budgets/{budget_id}")
        return BudgetDetailResponse.from_dict(response)

    def get_budget_settings(self, budget_id: str) -> BudgetSettingsResponse:
        response = self.client.get(f"/budgets/{budget_id}/settings")
        return BudgetSettingsResponse.from_dict(response)
