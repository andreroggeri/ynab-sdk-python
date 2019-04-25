from ynab_sdk_python.api.models.transactions import TransactionsResponse
from ynab_sdk_python.utils.api_client import ApiClient


class TransactionsApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def get_transcations(self, budget_id: str) -> TransactionsResponse:
        response = self.client.get(f'/budgets/{budget_id}/transactions')
        return TransactionsResponse.from_dict(response)

    def create_transactions(self, budget_id: str, transactions):
        payload = {
            'transactions': transactions
        }
        return self.client.post(f'/budgets/{budget_id}/transactions', payload)
