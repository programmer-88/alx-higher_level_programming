#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

if __name__ == '__main__':
    if len(sys.argv) == 4:
        ag_1 = int(sys.argv[1])
        ag_2 = sys.argv[2]
        ag_3 = int(sys.argv[3])

        if sys.argv[2] == "+":
            result = add(int(sys.argv[1]), int(sys.argv[3]))
            print("{:d} {} {:d} = {:d}".format(ag_1, ag_2, ag_3, result))
        elif sys.argv[2] == "-":
            result = sub(int(sys.argv[1]), int(sys.argv[3]))
            print("{:d} {} {:d} = {:d}".format(ag_1, ag_2, ag_3, result))
        elif sys.argv[2] == "*":
            result = mul(int(sys.argv[1]), int(sys.argv[3]))
            print("{:d} {} {:d} = {:d}".format(ag_1, ag_2, ag_3, result))
        elif sys.argv[2] == "/":
            result = div(int(sys.argv[1]), int(sys.argv[3]))
            print("{:d} {} {:d} = {:d}".format(ag_1, ag_2, ag_3, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")

    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
