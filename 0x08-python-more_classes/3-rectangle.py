#!/usr/bin/python3

""" This class efines a rectangle"""


class Rectangle:
    """ This class implements a rectangle"""

    def __init__(self, width=0, height=0):
        """intitializing rectangle width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.__width * self.__height
    
    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.height is 0:
            perimeter = 0
        elif self.width is 0:
            perimeter = 0
        else:
            perimeter = (self.width * 2) + (self.height * 2)
