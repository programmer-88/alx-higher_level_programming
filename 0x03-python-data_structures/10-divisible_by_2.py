#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return []
    else:
        return [True if div % 2 == 0 else False for div in my_list]
