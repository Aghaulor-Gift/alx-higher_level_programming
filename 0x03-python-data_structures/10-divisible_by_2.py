#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []

    for index in range(len(my_list)):
        index_value = my_list[index]
        if index_value % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
