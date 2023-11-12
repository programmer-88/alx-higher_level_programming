#!/usr/bin/python3

"""
Module for Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x position of rectangle
            y (int): y position of rectangle
            id (int): id of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for width

        Returns:
            width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width

        Args:
            value (int): width of rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter for height

        Returns:
            height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height

        Args:
            value (int): height of rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Getter for x

        Returns:
            x position of rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x

        Args:
            value (int): x position of rectangle

        Raises:
            TypeError: if x is not an integer
            ValueError: if x is < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter for y

        Returns:
            y position of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y

        Args:
            value (int): y position of rectangle

        Raises:
            TypeError: if y is not an integer
            ValueError: if y is < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """area of rectangle"""
        return self.__height * self.__width
    
    def display(self):
        """display of rectangle"""
        for i in int(Rectangle.area):
            print("#")
