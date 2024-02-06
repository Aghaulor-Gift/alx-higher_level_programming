#!/usr/bin/python3
"""
Defines a Student class with instance attributes and methods.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with a first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): List of attribute names to retrieve.\
            If None, retrieve all attributes.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if
                    hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those\
        from a provided dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
