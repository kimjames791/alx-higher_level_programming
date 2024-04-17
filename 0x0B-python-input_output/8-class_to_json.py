#!/usr/bin/python3
""" this Contains the "class_to_json" function"""


def class_to_json(obj):
    """ it returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of objects"""
    return obj.__dict__
