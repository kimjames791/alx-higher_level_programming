#!/usr/bin/python3
"""This defines an append_write function"""


def append_write(filename="", text=""):
    """it appends a filename with utf-8"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
