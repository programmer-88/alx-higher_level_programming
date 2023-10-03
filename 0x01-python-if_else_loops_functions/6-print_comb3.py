#!/usr/bin/python3
for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        print("{:02d}, ".format(digit1 * 10 + digit2), end='')
