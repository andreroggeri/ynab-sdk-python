import requests

from ynab_sdk.utils.clients.base_client import BaseClient
from ynab_sdk.utils.configurations.default import DefaultConfig


class DefaultClient(BaseClient):
    def __init__(self, config: DefaultConfig):
        super().__init__(config)

    def get(self, endpoint: str):
        url = self.config.full_url + endpoint
        self.logger.debug(f"Sending get at  {url}")
        response = requests.get(url, headers=self.headers)
        data = response.json()

        return data

    def post(self, endpoint: str, payload: dict):
        url = self.config.full_url + endpoint
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def put(self, endpoint: str, payload: dict):
        url = self.config.full_url + endpoint
        response = requests.put(url, json=payload, headers=self.headers)
        return response.json()
