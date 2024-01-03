#!/usr/bin/python3
def uppercase(str):
    for char in str:
        upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(upper_char), end="")
    print()


if __name__ == "__main__":
    uppercase("holberton")
    uppercase("Holberton School")
    uppercase("Holberton School, 98 battery street")
    uppercase("")
    uppercase("98")
    uppercase("z")
