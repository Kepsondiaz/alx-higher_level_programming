#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list 
    else: 
        copy_list = my_list.copy()
        copy_list[idx] = element
        return copy_list 

