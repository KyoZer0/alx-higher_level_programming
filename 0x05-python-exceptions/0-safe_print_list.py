#!/usr/bin/python3

def safe_print_list(my_list=[], n=0):
    nb_print = 0
    for i in range(n):
        try:
            print(my_list[i], end='')
            nb_print += 1
        except IndexError:
            break
    print()
    return nb_print
