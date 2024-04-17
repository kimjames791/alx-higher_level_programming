#!/usr/bin/python3
"""This defines a read_file function"""


def read_file(filename=""):
    """ it reads a filename with utf-8"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
