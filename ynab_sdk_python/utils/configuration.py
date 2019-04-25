class Configuration:
    def __init__(self):
        self.api_key = None
        self.base_path = '/v1'
        self.host = 'https://api.youneedabudget.com'

    @property
    def full_url(self):
        return self.host + self.base_path
