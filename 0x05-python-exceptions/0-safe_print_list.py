#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed_element = 0
        for i in range(x):
            print(my_list[i], end="")
            printed_element += 1
        print()
        return printed_element
    except (IndexError, NameError):
        print()
        return printed_element
