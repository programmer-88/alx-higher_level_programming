#!/usr/bin/python3

"""An empty BaseGeometry"""


class BaseGeometry:
    """
        class with public attributes area
    """
    def area(self):
        """
            raises an exeption error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be grater than 0")
