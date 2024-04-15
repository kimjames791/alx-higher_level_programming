#!/usr/bin/python3
"""
contains MyList class
"""


class MyList(list):
    """my subclass of list"""
    def __init__(self):
        """initializes  object"""
        super().__init__()

    def print_sorted(self):
        """prints my sorted list"""
        print(sorted(self))
