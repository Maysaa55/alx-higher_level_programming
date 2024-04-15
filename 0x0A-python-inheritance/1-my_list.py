#!/usr/bin/python3
""" Defines an inherted class my list."""

class MyList(list):
    """ defines a method that return a sorted list"""

    def print_sorted(self):
        """defines a method for sorted list"""

        return(sorted(self))
