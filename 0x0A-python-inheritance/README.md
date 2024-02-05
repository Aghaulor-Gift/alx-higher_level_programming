# Python Inheritance Project

## Overview

This Python project demonstrates the concept of inheritance in object-oriented programming.
It includes a base class and a derived class that inherits from the base class.

## Project Structure

- `parent_class.py`: Contains the definition of the parent class `Parent`.
- `child_class.py`: Contains the definition of the derived class `Child`.
- `main.py`: Demonstrates the usage of inheritance by creating instances of the `User` class.

## Parent Class - `Parent`

The `Parent` class serves as the parent class with the following features:
- Class attribute `__nb_instances` to count the number of instances.
- `__init__` method to initialize the instance and assign a unique `id`.

## Derived Class - `Child`

The `child` class inherits from the `Child` class and introduces the following modifications:
- Overrides the `__init__` method using `super().__init__()` to inherit the initialization logic from the base class.
- Adds additional functionality by modifying the `id` attribute.
