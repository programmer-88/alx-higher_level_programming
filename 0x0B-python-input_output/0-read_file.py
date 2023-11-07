#!/usr/bin/python3
""" reads text file UTF8 encoding and prints to stdout """


def read_file(filename=""):
    """ reads text file UTF8 encoding and prints to stdout
        Args:
             filename: string to read and print
             Returns: nothing
    """

    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end="")
