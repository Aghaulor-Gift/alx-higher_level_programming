#!/usr/bin/python3
def uppercase(str):
    for char in str:
        upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(upper_char), end="")
    print()


uppercase("holberton")
uppercase("Holberton School")
uppercase("Holberton School 98 Battery street")
