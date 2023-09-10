#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
    else:
        for i in range(0, len(matrix)):
            for j in matrix[i]:
                print("{:d}".format(j), end=" ")
            print()
