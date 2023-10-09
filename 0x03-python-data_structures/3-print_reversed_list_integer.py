#!/usr/bin/python3

def print_reversed_list(my_list=[]):
    if not my_list:
        pass
    else:
        my_list.reverse()
        for n in my_list:
            print("{:d}".format(n))
