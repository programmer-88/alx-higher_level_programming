#!/usr/bin/python3

""" This module defines a class square """


class Square:
    """ Square class with a private instance attribute"""

    def __init__(self, size=0):

        """ Initialize square size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size
