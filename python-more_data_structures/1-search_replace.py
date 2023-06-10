#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None:
        return my_list

    if len(my_list) == 0:
        return my_list

    newlist = my_list.copy()

    for i in range(len(newlist)):
        if newlist[i] == search:
            newlist[i] = replace

    return newlist
