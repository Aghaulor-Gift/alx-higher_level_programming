#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    all_element = set()
    for element in set_1 ^ set_2:
        all_element.add(element)
    return all_element
