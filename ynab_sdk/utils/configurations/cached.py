from ynab_sdk.utils.configurations.default import DefaultConfig


class CachedConfig(DefaultConfig):

    def __init__(self, redis_host: str, redis_port: int, redis_db: int = 0, redis_pass: str = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.redis_pass = redis_pass
