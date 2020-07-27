import json

import requests
from redis import Redis

from ynab_sdk.utils.clients.base_client import BaseClient
from ynab_sdk.utils.configurations.cached import CachedConfig


class CachedClient(BaseClient):

    def __init__(self, config: CachedConfig):
        super().__init__(config)
        self.redis = Redis(host=config.redis_host, port=config.redis_port, db=config.redis_db, password=config.redis_pass)
        self._redis_ttl_default = 3600
        self._redis_ttl = self._redis_ttl_default
        self._redis_prefix: str = 'YNAB_endpoint_'

    @property
    def cache_time_to_live(self) -> int:
        return self._redis_ttl

    @cache_time_to_live.setter
    def cache_time_to_live(self, ttl_value: int) -> None:
        if ttl_value and ttl_value > 0:
            self._redis_ttl = ttl_value
        else:
            self.logger.error(f'cache_time_to_live: invalid TTL value: {ttl_value}, using default')
            self._redis_ttl = self._redis_ttl_default

    def clear_cache(self) -> None:
        keys_count: int = 0
        for k in self.redis.scan_iter(''.join([self._redis_prefix, '*'])):
            self.redis.delete(k)
            keys_count += 1
        self.logger.error(f'clear_cache: {keys_count} keys deleted from cache')

    def get(self, endpoint: str):
        self.logger.error(f'Endpoint => {endpoint}')
        cached_data = self.redis.get(''.join([self._redis_prefix, endpoint]))

        if cached_data:
            self.logger.error('Using cached data')
            data = json.loads(cached_data)
        else:
            self.logger.error('Cached data not found, searching for new one')
            url = self.config.full_url + endpoint
            self.logger.debug(f'Sending get at {url}')
            response = requests.get(url, headers=self.headers)
            data = response.json()
            if response.status_code == 200:
                self.redis.set(''.join([self._redis_prefix, endpoint]), json.dumps(data), self._redis_ttl)
            else:
                self.logger.error(f'Error when getting {url}')
                self.logger.error(data)

        return data

    def post(self, endpoint: str, payload: dict):
        url = self.config.full_url + endpoint
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()
