#!/usr/bin/python3
""" Module for Pascal Triangle """


def pascal_triangle(n):
    """
    pascal_triangle - Prints a pascal triangle using lists
    ---------------

    Parameter:

    @n: Number of rows
    ---------------

    Return: A list of lists (Matrix)
    """
    pasc = []
    if n > 0:
        for i in range(n):
            pasc.append([1])
            if i > 1:
                for k in range(1, len(pasc[i - 1])):
                    pasc[i].append(pasc[i - 1][k - 1] + pasc[i - 1][k])
            if i > 0:
                pasc[i].append(1)
    return pasc
