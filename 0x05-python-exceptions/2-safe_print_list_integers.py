#!/usr/bin/python3


def safe_print_list_integers(my_list=[], n=0):
    printed = 0
    for i in range(n):
        try:
            print('{:d}'.format(my_list[i]), end='')
            printed += 1
        except (TypeError, ValueError):
            pass

    print()
    return printed
