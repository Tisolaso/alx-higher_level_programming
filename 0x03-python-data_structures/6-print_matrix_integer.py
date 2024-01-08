#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for index, int in enumerate(list):
            print("{:d}".format(int), end="")
            if index != (len(list)-1):
                print("{}".format(" "),end="")
        print()

