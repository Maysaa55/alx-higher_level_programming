#!/usr/bin/python3
"""function determine if the object is an instance of a class."""

def is_kind_of_class(obj, a_class):
    """ determine if the instance is the class or subclass object.
    Args:
    obj (any): the object to check.
    a_class (type): a
    the class to match the object to.
    Returns:
    True - if the object match
    False - otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
