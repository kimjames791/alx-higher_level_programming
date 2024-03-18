#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for k in my_string:
        if k != 'C' and k != 'c':
            new_str += k

    return new_str
