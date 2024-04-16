#!/usr/bin/python3
"""defines a function write json string to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """function's representation.
    Args:
    my_obj (any): the object to convert.
    filename (any): the file to write the json representation to .
    Returns:
    nothing.
    """

    with open(filename, mode='w', encoding="utf-8") as fl:
        fl.write(json.dumps(my_obj))
