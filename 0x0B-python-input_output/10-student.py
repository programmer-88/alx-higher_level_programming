#!/usr/bin/python3

"""Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """initialize attributes
            Args:
                first_name: f_name of the student
                Last_name: f_name of the student
                age: age of the student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of Student.
            Args:
                attr (list): attribute names that are to be retrieved.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
