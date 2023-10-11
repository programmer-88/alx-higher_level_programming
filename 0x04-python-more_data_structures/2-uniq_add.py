#!/usr/bin/python3

def uniq_add(input_list):
    unique_set = set()
    total = 0

    for num in input_list:
        if num not in unique_set:
            unique_set.add(num)
            total += num

    return total
