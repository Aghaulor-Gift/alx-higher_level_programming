#!/usr/bin/python3
"""A module that defines the class MyList that inherits from list"""


class MyList(list):
    """Custom class MyList that inherits from list."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
