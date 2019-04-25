from ynab_sdk_python.api.models.payee import PayeeResponse
from ynab_sdk_python.api.models.payees import PayeesResponse
from ynab_sdk_python.utils.api_client import ApiClient


class PayeeApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def get_payees(self, budget_id: str) -> PayeesResponse:
        response = self.client.get(f'/budgets/{budget_id}/payees')
        return PayeesResponse.from_dict(response)

    def get_payee(self, budget_id: str, payee_id: str) -> PayeeResponse:
        response = self.client.get(f'/budgets/{budget_id}/payees/{payee_id}')
        return PayeeResponse.from_dict(response)
