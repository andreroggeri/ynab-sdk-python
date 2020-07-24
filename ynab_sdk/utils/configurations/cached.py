from ynab_sdk.utils.configurations.default import DefaultConfig
from typing import Union


class CachedConfig(DefaultConfig):

    def __init__(self, redis_host: str, redis_port: int, redis_db: int = 0, **kwargs) -> None:
        super().__init__(**kwargs)
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self._redis_TTL: Union[int, None] = 3600

    @property
    def redis_TTL(self) -> Union[int, None]:
        return self._redis_TTL

    @redis_TTL.setter
    def redis_TTL(self, TTL_value: Union[int, None]) -> None:
        self._redis_TTL = TTL_value
