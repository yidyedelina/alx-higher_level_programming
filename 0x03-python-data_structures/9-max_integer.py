#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if len(my_list) == 0:
        return None
    for li in my_list:
        if max <= li:
            max = li
    return max
