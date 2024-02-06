#!/usr/bin/python3
""" A module that defines a class MyInt that inherits from int
"""


class MyInt(int):
    """A class representing a rebellious integer."""

    def __eq__(self, other):
        """Override the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator."""
        return super().__eq__(other)
