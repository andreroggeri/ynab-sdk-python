from ynab_sdk_python.api.accounts import AccountsApi
from ynab_sdk_python.api.budgets import BudgetsApi
from ynab_sdk_python.api.categories import CategoriesApi
from ynab_sdk_python.api.payees import PayeeApi
from ynab_sdk_python.api.transactions import TransactionsApi
from ynab_sdk_python.utils.api_client import ApiClient
from ynab_sdk_python.utils.configuration import Configuration


class YNAB:

    def __init__(self, api_key: str):
        config = Configuration()
        config.api_key = api_key
        config.base_path = '/v1'

        self.client = ApiClient(config)

    @property
    def budgets(self):
        return BudgetsApi(self.client)

    @property
    def accounts(self):
        return AccountsApi(self.client)

    @property
    def categories(self):
        return CategoriesApi(self.client)

    @property
    def payees(self):
        return PayeeApi(self.client)

    @property
    def transactions(self):
        return TransactionsApi(self.client)
