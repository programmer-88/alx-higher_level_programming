#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
str = "Last digit of "
if ld == 0:
    print("{}{} is {} and is {}".format(str, number, ld, ld))

elif ld > 5:
        print("{}{} is {} and is greater than 5".format(str, number, ld))

else:
    print("{}{} is {} and is less than 5".format(str,number , ld))