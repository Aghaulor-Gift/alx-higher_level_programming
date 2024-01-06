#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []

    for i in range(2):
        element_a = tuple_a[i] if i < len(tuple_a) else 0
        element_b = tuple_b[i] if i < len(tuple_b) else 0
        result.append(element_a + element_b)

    return tuple(result)
