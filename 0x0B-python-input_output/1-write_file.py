#!/usr/bin/python3
"""This defines a write_file with two arguments"""


def write_file(filename="", text=""):
    """ it will read a filename with utf-8"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
