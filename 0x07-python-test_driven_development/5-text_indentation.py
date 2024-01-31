#!/usr/bin/python3
"""
    Prints text indentation

    Parameters:
    - text (str): The input text.

    Raises:
    TypeError: If text is not a string.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    current_line = ""

    for char in text:
        current_line += char

        if char in ['.', '?', ':']:
            print(current_line)

            print("\n" * 2)

            current_line = ""

    if current_line:
        print(current_line)
