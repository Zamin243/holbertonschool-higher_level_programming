#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    salam = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            salam.append(True)
        else:
            salam.append(False)
    return salam
