#!/usr/bin/python3
first_combination = True

for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        if not first_combination:
            print(", ", end='')
        else:
            first_combination = False
        print("{:02d}".format(digit1 * 10 + digit2), end='')
