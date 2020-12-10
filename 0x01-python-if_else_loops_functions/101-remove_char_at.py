#!/usr/bin/python3
def remove_char_at(str, n):
    j = ""
    for i in str:
        if i != n:
            j += str[i]
    return (j)
