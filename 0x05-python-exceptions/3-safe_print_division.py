#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        if b != 0:
            print("Inside result: {}".format(result))
            return "{}".format(result)
        print("{:d} / {:d} = {}".format(a, b, result))
    except ZeroDivisionError:
        print("Inside result: {}".format(result))
        return "{}".format(result)
    print("{:d} / {:d} = {}".format(a, b, result))
