#!/usr/bin/python3
def uppercase(s):
    for char in s:
        upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(upper_char), end="")
    print()


uppercase("holberton")
uppercase("Holberton School")
uppercase("Holberton School 98 Battery street")


def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
