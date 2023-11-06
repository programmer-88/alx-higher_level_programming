#!/usr/bin/python3

""" returs true if object is an instance of
    or object is an instance of a class inherited from"""


def is_kind_of_class(obj, a_class):
    """
        Args:
             obj: initial object
             a_class: object to check
             Returns: true if obj is instance or instance
                      of a class inherited from
    """
    return isinstance(obj, a_class)
