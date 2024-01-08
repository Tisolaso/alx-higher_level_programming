#!/usr/bin/python3

def element_at(list=[], index=0):
    if len(list) <= index or index < 0:
        return None

    return list[index]
