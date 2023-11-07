#!/usr/bin/python3
""" reads text file UTF8 encoding and prints to stdout """


def read_file(filename=""):
    """ reads text file UTF8 encoding and prints to stdout """

    with open(filename, "r", encoding='utf-8') as file:
        for line in file:
            print(line)
