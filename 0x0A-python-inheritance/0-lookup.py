#!/usr/bin/python3
""" This module returns the list of available attributes and methods
    of an object"""


def lookup(obj):
    """
    Args:
        obj: initialized object
        Returns: list of attributes and methods
                 of a given object
    """
    return dir(obj)
