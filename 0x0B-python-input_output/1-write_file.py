#!/usr/bin/python3
""" This module Write File """


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
        returns the number of characters written.
    """

    with open(filename, mode='w', encoding='utf-8') as file:
        characters_written = file.write(text)
    return characters_written


if __name__ == "__main__":
    filename = "my_first_file.txt"
    text = "This School is so cool!\n"
    character_count = write_file(filename, text)
    print(character_count)
