#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        temp[idx] = element
        return temp
