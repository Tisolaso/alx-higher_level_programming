#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for int in list:
            print("{:d}".format(int), end="")
        print("$")
