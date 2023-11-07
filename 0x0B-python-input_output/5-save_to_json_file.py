#!/usr/bin/python3

"""write json representation of obj to file"""

import json


def save_to_json_file(my_obj, filename):
    """write json representation"""

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
