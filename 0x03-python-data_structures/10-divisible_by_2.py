#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_multiples.append(True)
        else:
            list_multiples.append(False)
    return list_multiples
