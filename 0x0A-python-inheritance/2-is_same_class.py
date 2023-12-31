#!/usr/bin/python3
"""returns true if object is exactly an instance of
    specified class"""


def is_same_class(obj, a_class):
    """
        Args:
            obj: initialized object
            a_class: object to compare against
            Returns: true if obj is exactly a class
        """

    return type(obj) is a_class
