from typing import Optional, Union

from ynab_sdk.utils.configurations.default import DefaultConfig


class CachedConfig(DefaultConfig):
    def __init__(
        self,
        redis_host: str,
        redis_port: int,
        redis_db: int = 0,
        redis_pass: Optional[str] = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.redis_pass = redis_pass
        self._redis_ttl: Optional[int] = 3600

    @property
    def redis_ttl(self) -> Optional[int]:
        return self._redis_ttl

    @redis_ttl.setter
    def redis_ttl(self, ttl_value: Optional[int]) -> None:
        if ttl_value and ttl_value > 0:
            self.logger.debug(f"redis_ttl: TTL value set to {ttl_value}")
            self._redis_ttl = ttl_value
        else:
            self.logger.debug(
                f"redis_ttl: 0, negative or None TTL value: {ttl_value}, set to None"
            )
            self._redis_ttl = None
