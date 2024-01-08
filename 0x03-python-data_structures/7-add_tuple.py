#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = []

    for i in range(0, len(tuple_a)):

        tuple_1 = tuple_a + (0, 0)
        tuple_2 = tuple_b + (0, 0)

        sum.append(tuple_1[i] + tuple_2[i])

    return tuple(sum)
