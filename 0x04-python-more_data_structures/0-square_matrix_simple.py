#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for list in matrix:
        item = [*map(lambda int: int * int, list)]
        new_matrix.append(item)

    return new_matrix
