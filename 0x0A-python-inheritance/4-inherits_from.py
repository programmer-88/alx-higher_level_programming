#!/usr/bin/python3

""" returns true if object is an instance of a class inherited"""


def inherits_from(obj, a_class):
    """
        Args:
             obj: initial object
             a_class: object to compare
             Returns: true if obj is a subclass of a class
    """
    return issubclass(type(obj), a_class)
