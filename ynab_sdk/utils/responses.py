def json_response(fn: callable):
    def wrapper(*args):
        return fn(*args)

    return wrapper
