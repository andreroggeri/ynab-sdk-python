from ynab_sdk_python.api.models.account import AccountResponse
from ynab_sdk_python.api.models.accounts import AccountsResponse
from ynab_sdk_python.utils.api_client import ApiClient


class AccountsApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def get_accounts(self, budget_id: str) -> AccountsResponse:
        response = self.client.get(f'/budgets/{budget_id}/accounts')
        return AccountsResponse.from_dict(response)

    def get_account(self, budget_id: str, account_id: str) -> AccountResponse:
        response = self.client.get(f'/budgets/{budget_id}/accounts/{account_id}')
        return AccountResponse.from_dict(response)
