#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True

    except (ValueError,TypeError) as e:
        from sys import stderr
        stderr.write("Exceprion: {}\n".format(e))
        return False
