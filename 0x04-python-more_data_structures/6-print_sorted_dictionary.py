#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list1 = list(a_dictionary.keys())
    list1.sort()
    sorted_dict = {i: a_dictionary[i] for i in list}
    return sorted_dict
