#!/usr/bin/python3
"""defines the class rectangle."""

class Rectangle(BaseGeometry):
    """represent the rectangle class"""

    def __init__(self, width, height):
        """ make a construct for the rectangle class."""
        if type(width) is int() and width > 0:
        self.__width = width
        if type(height) is int() and height > 0:
        self.__height = height
