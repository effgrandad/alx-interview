#!/usr/bin/python3

"""
Develop a function that gives back a list of lists of integers that
represent n Pascal's triangles.

"""


def pascal_triangle(n: int) -> list:
    """
    Returns a list of list of intergers
    Args:
        n (int): size of the triangles
    Returns:
        list
    """
    if not isinstance(n, int):
        raise TypeError(f"{n} is not an integer")
    if n <= 0:
        return ([])
    triangles = []
    for h in range(n):
        temp = []

        for j in range(h+1):
            if j == 0 or j == h:
                temp.append(1)
            else:
                temp.append(triangles[h-1][j-1] + triangles[h-1][j])
        triangles.append(temp)
    return triangles
