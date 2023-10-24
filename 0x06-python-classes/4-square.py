#!/usr/bin/python3

""" This module defines a class square """


class Square:
    """ Square class with a private instance attribute"""

    def __init__(self, size=0):
        """ 
        initialize attribute
        
        Args:
            size: size of square
        """

        self.size = size

        @property
        def size(self):
            return self.__size
        
        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            
            if value < 0:
                raise ValueError("value must be >= 0")
            self.__size = value

        def area(self):
            return self.__size ** 2
