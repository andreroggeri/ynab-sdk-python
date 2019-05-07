import json

import requests
from redis import Redis

from ynab_sdk.utils.clients.base_client import BaseClient
from ynab_sdk.utils.configurations.cached import CachedConfig


class CachedClient(BaseClient):

    def __init__(self, config: CachedConfig):
        super().__init__(config)
        self.redis = Redis(host=config.redis_host, port=config.redis_port, db=config.redis_db)

    def get(self, endpoint: str):
        self.logger.error(f'Endpoint => {endpoint}')
        cached_data = self.redis.get(endpoint)

        if cached_data:
            self.logger.error('Using cached data')
            data = json.loads(cached_data)
        else:
            self.logger.error('Cached data not found, searching for new one')
            url = self.config.full_url + endpoint
            self.logger.debug(f'Sending get at  {url}')
            response = requests.get(url, headers=self.headers)
            data = response.json()
            if response.status_code == 200:
                self.redis.set(endpoint, json.dumps(data))
            else:
                self.logger.error(f'Error when getting {url}')
                self.logger.error(data)

        return data

    def post(self, endpoint: str, payload: dict):
        url = self.config.full_url + endpoint
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()
