#!/usr/bin/python3

"""Module for Rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectange class that inherits from BaseGeometry
        Args:
             width: The width of the rectangle
             height: The height of the rectangle
    """
    def __init__(self, width, height):
        self.integer_validator ("width", width)
        self.integer_validator ("height", height)

        self.__width = width
        self.__height = height
