class YNABException(Exception):
    def __init__(self, http_code: int, content: dict):
        self.http_code = http_code
        self.content = content
