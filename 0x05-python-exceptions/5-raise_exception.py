#!/usr/bin/python3
def raise_exception():
    try:
        raise Exception
    except TypeError as te:
        print("Exception raised")
