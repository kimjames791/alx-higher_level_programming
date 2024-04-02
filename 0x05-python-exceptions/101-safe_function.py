#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ans = fct(*args)
    except ZeroDivisionError:
        ans = None
        sys.stderr.write("Exception: division by zero\n")
    except IndexError:
        ans = None
        sys.stderr.write("Exception: list index out of range\n")

    return ans
