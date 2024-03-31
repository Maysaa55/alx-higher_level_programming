#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list1 = list(a_dictionary.keys())
    list1.sort()
    for item in list1:
        print(item+": ", a_dictionary[item])
    return 0
