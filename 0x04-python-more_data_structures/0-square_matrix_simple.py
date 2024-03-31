#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list1 = []
    list2 = []
    for i in matrix:
        for item in i:
            list1.append(item**2)
        list2.append(list1)
        for item in list1:
            list1.pop(0)
    return list2
