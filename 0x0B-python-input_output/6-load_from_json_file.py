#!/usr/bin/python3
""" a function defining load_from_json_file"""


import json


def load_from_json_file(filename):
    """ this creates an object from json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
