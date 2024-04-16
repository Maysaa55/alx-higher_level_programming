#!/usr/bin/python3
""" defines a function reads a file and print it."""

def read_file(filename=""):
    """representing the function.
    Args:
    filename (any): the name of the file to be read;
    """
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
