#!/usr/bin/python
def common_elements(set_1, set_2):
    common_set = set()
    for element in set_1 and set_2:
        if element in set_1 and element in set_2:
            common_set.add(element)
    return common_set
