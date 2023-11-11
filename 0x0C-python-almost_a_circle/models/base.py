#!/usr/bin/python3

"""Base class for all objects in this project"""
class Base:
    """Thsi is a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Create a new instance"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1 
            self.id = Base.__nb_objects
