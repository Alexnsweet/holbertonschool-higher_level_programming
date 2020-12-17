#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        number = 0
        new_list = my_list[:]
        new_list.sort()

        for i in range(len(new_list)):
            if new_list[i] != new_list[i - 1]:
                number += new_list[i]
        return number
