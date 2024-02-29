# print all the sublists of the list given.

from itertools import combinations

list1 = [20, 30, 40, 50]
list2 = ['a', 'b', 'c']


def sub_lists(item):
    subs = []
    for i in range(0, len(item) + 1):
        temp = [list(x) for x in combinations(item, i)]
        if len(temp) > 0:
            subs.extend(temp)
        else:
            pass

    return subs

    print(f'the sublists of the list {item} are : {subs}')


sub_lists(list1)
