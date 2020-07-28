def build_get_mock(return_value):
    def mock_get(_self, _endpoint):
        return return_value

    return mock_get


def build_post_mock():
    def mock_post(_self, _endpoint, _payload):
        return {}

    return mock_post


def build_put_mock():
    def mock_put(_self, _endpoint, _payload):
        return {}

    return mock_put
