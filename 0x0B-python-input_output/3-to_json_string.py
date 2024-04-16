#!/usr/bin/python3
""" Define a function returns the json of an object."""
import json


def to_json_string(my_obj):
    """represents the function.
    Args:
    my_obj (any): the onject to convert to json.
    Returns:
    the json representation to the object.
    """

    return json.dumps(my_obj)
