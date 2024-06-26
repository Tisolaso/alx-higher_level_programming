#!/usr/bin/python3
""" find peak module """


def find_peak(list_of_integers):
    """ find peak function"""
    if list_of_integers:
        lf = 0
        r = len(list_of_integers) - 1
        while lf < r:
            m = (lf + r) // 2
            if list_of_integers[m] > list_of_integers[m + 1]:
                r = m
            else:
                lf = m + 1
        return list_of_integers[lf]
