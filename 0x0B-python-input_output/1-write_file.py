#!/usr/bin/python3
"""Defines function that wrie to a file"""


def write_file(filename="", text=""):
    """ represent the function.
    Args:
    filename (any): the name of the file to write in .
    text (any): the text to write in the file.
    Returns:
    the number of characters added to the file.
    """

    with open(filename, mode= 'w', encoding= "utf-8") as fl:
        return (fl.write(text))
