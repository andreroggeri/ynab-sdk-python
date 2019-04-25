import json
import logging

import requests
from redis import Redis

from ynab_sdk_python.utils.configuration import Configuration


class ApiClient:
    logger = logging.getLogger(__name__)

    def __init__(self, config: Configuration):
        self.config = config
        self.redis = Redis(host='localhost', port=6379, db=0)

    def get(self, endpoint: str):
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
            self.redis.set(endpoint, json.dumps(data))

        return data

    def post(self, endpoint: str, payload: dict):
        url = self.config.full_url + endpoint
        self.logger.debug(f'Sending get at  {url} with the payload {payload}')

    @property
    def headers(self):
        return {
            'Authorization': f'Bearer {self.config.api_key}',
            'accept': 'application/json'
        }
