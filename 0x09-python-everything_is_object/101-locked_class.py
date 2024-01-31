#!/usr/bin/python3
"""This is a Locked class module.
Attributes:
    LockedClass: A class that restricts dynamic creation of instance attributes.
"""


class LockedClass:
    """Represent a LockedClass"""
    __slots__ = ('first_name',)
