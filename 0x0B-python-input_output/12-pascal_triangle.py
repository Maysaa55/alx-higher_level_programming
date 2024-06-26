#!/usr/bin/python3
""" defines the pascal's triangle function."""


def pascal_triangle(n):
    """ reoresent the function.

    Args:
    n (any): the number.

    Returns:
    a list of lists of integers represent the triangle.
    """

    lst = []
    if n <= 0:
        return lst
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
