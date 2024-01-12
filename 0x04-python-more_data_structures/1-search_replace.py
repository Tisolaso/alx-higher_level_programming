#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = map(lambda int : replace if int == search else int, my_list)
    return [*new_list]
