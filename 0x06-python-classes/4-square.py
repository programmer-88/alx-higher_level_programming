#!/usr/bin/python3

""" This module defines a class square """


class Square:
    """ Square class with a private instance attribute"""

    def __init__(self, size=0) -> None:
        """ 
        initialize attribute
        
        Args:
            size: size of square
        """

        self.size = size

        @property
        def size(self):
            """ get attribute value to be used in class"""
            return self.__size
        
        @size.setter
        def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")

            if value < 0:
                raise ValueError("value must be >= 0")
            self.__size = value

        def area(self):
            """ area of square"""
            return self.__size ** 2
