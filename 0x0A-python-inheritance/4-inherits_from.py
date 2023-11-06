#!/usr/bin/python3

""" returns true if object is an instance of a class inherited"""


def inherits_from(obj, a_class):
    """
        Args:
             obj: initial object
             a_class: object to compare
             Returns: true if obj is a subclass of a class
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
