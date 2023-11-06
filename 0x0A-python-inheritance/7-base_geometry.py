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
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{name} must be grater than 0".format(name))
