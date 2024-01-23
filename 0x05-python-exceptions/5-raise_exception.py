#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("type exception")
    except TypeError as te:
        print("Exception raised")
