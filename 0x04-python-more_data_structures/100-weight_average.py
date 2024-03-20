#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    return sum([mul(p[0], p[1]) for p in my_list]) / sum(p[1] for p in my_list)


def mul(p, y):
    return p * y
