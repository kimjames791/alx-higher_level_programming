#!/usr/bin/python3
"""
This module contains the function is_same_class func
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, false if not"""
    return (type(obj) == a_class)
