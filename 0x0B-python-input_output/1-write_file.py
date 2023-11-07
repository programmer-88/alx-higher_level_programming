#!/usr/bin/python3
""" reads text file UTF8 encoding and returns number of characters """


def write_file(filename="", text=""):
    """ reads text file UTF8 encoding and return number of characters
        Args:
             filename: string to read
             text: string to write

        Returns: number of characters
    """

    with open(filename, mode="w", encoding='utf-8') as file:
        return file.write(text)
