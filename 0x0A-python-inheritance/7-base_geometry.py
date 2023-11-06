#!/usr/bin/python3

"""An empty BaseGeometry"""


class BaseGeometry:
    """
        class with public attributes area
    """
    def area(self):
        """
            calculate generic area of a geometry

            Raises:
            raises an exeption error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value passed to the method.

        Args:
        - name (str): The name of the variable to validate.
        - value (int): The value to validate.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{name} must be grater than 0".format(name))
