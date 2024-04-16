#!/usr/bin/python3
"""defines a class with a method of dict representation."""


class Student:
    """ the class student."""

    def __init__(self, first_name, last_name, age):
        """ the constructor method."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """retrieves a dictionary representation."""
        return self.__dict__
