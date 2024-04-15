#!/usr/bin/python3
"""defines the class rectangle."""

class Rectangle(BaseGeometry):
    """represent the rectangle class"""

    def __init__(self, width, height):
        """ make a construct for the rectangle class."""
        self.__width = width
        self.__height = height
