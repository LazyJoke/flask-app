import os


def get_environment(key, default=None):
    if not key:
        return default
    return os.environ.get(key, default)
