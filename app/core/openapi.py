# coding=utf-8
import glob
import six
from yaml import safe_load


def data_merge(a, b):
    if a is None or isinstance(a, (six.string_types, float, six.integer_types)):
        # border case for first run or if a is a primitive
        a = b
    elif isinstance(a, list):
        # lists can be only appended
        if isinstance(b, list):
            # merge lists
            a.extend(b)
        else:
            # append to list
            a.append(b)
    elif isinstance(a, dict):
        # dicts must be merged
        if isinstance(b, dict):
            for key in b:
                if key in a:
                    a[key] = data_merge(a[key], b[key])
                else:
                    a[key] = b[key]
    return a


def yaml_load(source, default_data=None):
    data = {}
    if default_data:
        data = default_data
    files = glob.glob(source, recursive=True)
    if files:
        for yaml_file in files:
            with open(yaml_file) as f:
                new_data = safe_load(f)
            if new_data is not None:
                data = data_merge(data, new_data)
    return data

