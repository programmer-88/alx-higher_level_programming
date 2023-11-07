#!/usr/bin/python3

"""write json representation of obj to file"""

import json


def load_from_json_file(filename):
    """write json representation"""

    with open(filename, 'r') as file:
        return json.load(file)
