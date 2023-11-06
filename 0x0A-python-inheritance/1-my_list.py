#!/usr/bin/python3

"""inherits from list"""


class MyList(list):
    """Class that ingerits from list"""

    def print_sorted(self):
        """print sorted list(ascending)"""
        print(sorted(list(self)))
