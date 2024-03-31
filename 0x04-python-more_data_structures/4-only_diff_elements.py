#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list1 = []
    for item in set_1:
        if item not in set_2:
            list1.append(item)
    for item in set_2:
        if item not in set_1:
            list1.append(item)
    return list1
