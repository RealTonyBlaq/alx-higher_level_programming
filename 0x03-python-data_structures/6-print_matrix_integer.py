#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
    else:
        for i in range(0, len(matrix)):
            count = 0
            for j in matrix[i]:
                print("{:d}".format(j), end="")
                if count != (len(matrix[i]) - 1):
                    print(" ", end="")
                count += 1
            print()
