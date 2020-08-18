import logging
from abc import ABC, abstractmethod

from ynab_sdk.utils.configurations.default import DefaultConfig


class BaseClient(ABC):
    def __init__(self, config: DefaultConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def get(self, endpoint: str):
        raise NotImplementedError()

    @abstractmethod
    def post(self, endpoint: str, payload: dict):
        raise NotImplementedError()

    @abstractmethod
    def put(self, endpoint: str, payload: dict):
        raise NotImplementedError()

    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.config.api_key}",
            "accept": "application/json",
        }
