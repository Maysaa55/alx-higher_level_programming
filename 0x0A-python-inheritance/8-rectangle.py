#!/usr/bin/python3
"""defines the class rectangle."""

class Rectangle(BaseGeometry):
    """represent the rectangle class"""

    def __init__(self, width, height):
        """ make a construct for the rectangle class."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
