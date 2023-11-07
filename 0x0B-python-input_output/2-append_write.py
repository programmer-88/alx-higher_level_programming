#!/usr/bin/python3

"""append a string at the end of a UTF-8 text file"""


def append_write(filename="", text=""):
    """append text to file"""

    with open(filename, mode="a", encoding='utf-8') as file:
        return file.write(text)
