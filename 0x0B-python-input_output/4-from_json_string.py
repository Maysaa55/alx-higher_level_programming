#!/usr/bin/python3
"""Defines a function return the json string to the real object."""


def from_json_string(my_str):
    """ represent the function.
    Args:
    my_str (any): the json string to convert.
    Returns:
    the real object.
    """

    return json.load(my_str)
