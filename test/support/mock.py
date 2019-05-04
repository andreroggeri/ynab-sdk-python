def build_get_mock(return_value):
    def mock_get(_self, _endpoint):
        return return_value

    return mock_get
