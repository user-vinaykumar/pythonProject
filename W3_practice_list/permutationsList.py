# write a program to print all the permutations of the list.

mall = [1,2,3]

import itertools

def permutaionList(item):
    print(list(itertools.permutations(item)))

permutaionList(mall)