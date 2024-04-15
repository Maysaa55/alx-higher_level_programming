#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """defines whether the value is integer or not.
        Args:
        name (any): the name of the var.
        value (any): the value of the var.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))

