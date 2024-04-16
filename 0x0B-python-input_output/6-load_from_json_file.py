#!/usr/bin/python3
"""define a function that creates an object from json file."""
import json


def load_from_json_file(filename):
    """ represent the function.
    Args:
    filename (any): the json file.
    Returns:
    nothing.
    """ 

    with open(filename, encoding= "utf-8") as fl:
        oobj = json.load()
