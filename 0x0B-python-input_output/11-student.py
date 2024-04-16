#!/usr/bin/python3
"""defines a class with a method of dict representation."""


class Student:
    """ the class student."""

    def __init__(self, first_name, last_name, age):
        """ the constructor method."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """ the attributes method."""

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
        
    def reload_from_json(self, json):
        """ the reload method."""

        for key, value in json.items():
            setattr(self, key, value)
