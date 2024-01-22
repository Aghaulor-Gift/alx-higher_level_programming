#!/usr/bin/python3
def safe_print_integer(value):
    try:
        for i in [value]:
            print("{:d}".format(i))
            return True
    except (ValueError, TypeError):
        return False
