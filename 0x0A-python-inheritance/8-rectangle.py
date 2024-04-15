#!/usr/bin/python3
"""defines the class rectangle."""

class Rectangle(BaseGeometry):
    """represent the rectangle class"""

    def __init__(self, width, height):
        """ make a construct for the rectangle class."""
        if integer_validator(width) == True:
            self.width = width
        if integer_validator(height) == True:
            self.height = height
