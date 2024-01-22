#!/usr/bin/python3
def safe_print_division(a, b):
    inside_result = None  # Initialize result to None
    try:
        inside_result = a / b
        if b != 0:
            print("Inside result: {}".format(inside_result))
            return "{}".format(inside_result)
        print("{:d} / {:d} = {}".format(a, b, inside_result))
    except ZeroDivisionError:
        print("Inside result: {}".format(inside_result))
        return "{}".format(inside_result)
    finally:
        return inside_result
