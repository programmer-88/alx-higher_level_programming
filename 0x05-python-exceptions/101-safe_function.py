#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        return fct(*args)

    except (Exception) as err:
        from sys import stderr
        stderr.write("Exception: {}\n".format(err))
        return None
