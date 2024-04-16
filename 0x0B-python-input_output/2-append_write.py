#!/usr/bin/python3
"""Defines function that append to a file"""


def append_write(filename="", text=""):
    """ represent the function.
    Args:
    filename (any): the name of the file to append in .
    text (any): the text to append in the file.
    Returns:
    the number of characters added to the file.
    """
    with open(filename, mode= 'a', encoding= "utf-8") as fl:
        num = fl.append(text)
        return num
