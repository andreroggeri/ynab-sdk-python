class DefaultConfig:
    def __init__(
        self, api_key: str, base_path="/v1", host="https://api.youneedabudget.com"
    ):
        self.api_key = api_key
        self.base_path = base_path
        self.host = host

    @property
    def full_url(self):
        return self.host + self.base_path
