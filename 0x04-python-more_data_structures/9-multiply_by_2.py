#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()

    for p, o in b_dictionary.items():
        b_dictionary[p] = o * 2

    return b_dictionary
