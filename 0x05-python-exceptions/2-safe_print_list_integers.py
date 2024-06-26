#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    output = 0

    for k in range(x):
        try:
            if type(my_list[k]) is int and output != x:
                print('{:d}'.format(my_list[k]), end='')
                output += 1
        except TypeError:
            continue

    print()

    return output
