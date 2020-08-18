import json

import requests
from redis import Redis

from ynab_sdk.utils.clients.default_client import DefaultClient
from ynab_sdk.utils.configurations.cached import CachedConfig


class CachedClient(DefaultClient):
    def __init__(self, config: CachedConfig):
        super().__init__(config)
        self.redis = Redis(
            host=config.redis_host,
            port=config.redis_port,
            db=config.redis_db,
            password=config.redis_pass,
        )
        self._keys_prefix: str = "YNAB_ep_"

    def clear_cache(self) -> None:
        keys_count: int = 0
        for k in self.redis.scan_iter("".join([self._keys_prefix, "*"])):
            self.redis.delete(k)
            keys_count += 1
        self.logger.info(f"clear_cache: {keys_count} keys deleted from cache")

    def get(self, endpoint: str):
        self.logger.debug(f"Endpoint => {endpoint}")
        cached_data = self.redis.get("".join([self._keys_prefix, endpoint]))

        if cached_data:
            self.logger.info("Using cached data")
            data = json.loads(cached_data)
        else:
            self.logger.info("Cached data not found, searching for new one")
            url = self.config.full_url + endpoint
            self.logger.debug(f"Sending get at {url}")
            response = requests.get(url, headers=self.headers)
            data = response.json()
            if response.status_code == 200:
                self.redis.set(
                    "".join([self._keys_prefix, endpoint]),
                    json.dumps(data),
                    self.config.redis_ttl,
                )
            else:
                self.logger.error(f"Error when getting {url}")
                self.logger.error(data)

        return data
