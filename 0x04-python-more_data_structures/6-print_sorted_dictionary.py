#!/usr/bin/python3
print_sorted_dictionary(a_dictionary):
    list1 = list(a_dictionary.keys())
    list1.sort()
    sorted_dict = {}
    for item in list1:
        sorted_dict[item] = a_dictionary[item]
    return sorted_dict
