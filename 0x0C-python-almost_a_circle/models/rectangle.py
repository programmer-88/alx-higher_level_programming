#!/usr/bin/python3

"""This is a rectangle class"""

from models.base import Base

class Rectangle(Base):
    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        __width = width
        __height = height
        __x = x
        __y = y

        @property
        def width(self):
            return self.__width
        
        @width.setter
        def width(self, value):
            if value  < 0:
                raise ValueError("Width must be greater than zero")

            self.__width = value

        @property
        def height(self):
            return self.__height
        
        @height.setter
        def height(self, value):
            if value < 0:
                raise ValueError("Height must be greater than zero")
            
            self.__height = value

        @property
        def x(self):
            return self.__x
        
        @x.setter
        def x(self, value):
            if value < 0:
                raise ValueError("X must be non-negative")
            
            self.__x = value

        @property
        def y(self):
            return self.__y
        
        @y.setter
        def y(self, value):
            if value < 0:
                raise ValueError("Y must be non-negative")
