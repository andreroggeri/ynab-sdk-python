import dataclasses
from typing import List

from ynab_sdk.api.models.requests.transaction import TransactionRequest
from ynab_sdk.api.models.responses.transactions import TransactionsResponse
from ynab_sdk.api.models.responses.budget_detail import Transaction
from ynab_sdk.utils.clients.base_client import BaseClient


class TransactionsApi:

    def __init__(self, client: BaseClient):
        self.client = client

    def get_transactions(self, budget_id: str) -> TransactionsResponse:
        response = self.client.get(f'/budgets/{budget_id}/transactions')
        return TransactionsResponse.from_dict(response)

    def create_transactions(self, budget_id: str, transactions: List[TransactionRequest]):
        payload = {
            'transactions': [dataclasses.asdict(t) for t in transactions]
        }
        return self.client.post(f'/budgets/{budget_id}/transactions', payload)

    def update_transaction(self, budget_id: str, transaction: Transaction) -> TransactionsResponse:
        payload = {
                'transaction': dataclasses.asdict(transaction)
        }
        transaction_id = transaction.id
        response = self.client.put(f'/budgets/{budget_id}/transactions/{transaction_id}', payload)
        return response
