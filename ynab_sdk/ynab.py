from ynab_sdk.api.accounts import AccountsApi
from ynab_sdk.api.budgets import BudgetsApi
from ynab_sdk.api.categories import CategoriesApi
from ynab_sdk.api.payees import PayeeApi
from ynab_sdk.api.transactions import TransactionsApi
from ynab_sdk.utils.clients.base_client import BaseClient
from ynab_sdk.utils.clients.default_client import DefaultClient
from ynab_sdk.utils.configurations.default import DefaultConfig


class YNAB:
    def __init__(self, api_key: str = None, client: BaseClient = None):
        assert api_key is not None or client is not None

        if client:
            self.client = client
        else:
            config = DefaultConfig(api_key)
            self.client = DefaultClient(config)

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
