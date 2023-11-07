#!/usr/bin/python3

"""return obj representation of json"""

import json


def from_json_string(my_str):
    """convert to obj representation"""
    return json.loads(my_str)
