from ynab_sdk.utils.clients.base_client import BaseClient
from ynab_sdk.utils.configurations.default import DefaultConfig


class DummyClient(BaseClient):
    def __init__(self):
        config = DefaultConfig("abc")
        super().__init__(config)
        self.get_data = None

    def configure_get(self, data: dict):
        self.get_data = data

    def get(self, endpoint: str):
        return self.get_data

    def post(self, endpoint: str, payload: dict):
        pass

    def put(self, endpoint: str, payload: dict):
        pass
