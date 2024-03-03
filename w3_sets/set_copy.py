# print the exact copy of the set.

set1 = {'red', 'green'}

def setCopy(item):
    set2 = set1.copy()
    print(f'the copy of {item} is : {set2}')

setCopy(set1)