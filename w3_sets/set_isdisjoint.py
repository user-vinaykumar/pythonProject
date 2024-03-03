# checks whether the set is disjoint of another.

set1 = {'red', 'green', 'purple', 'black', 'brown'}
set2 = {'black', 'brown', 'yellow', 'orange', 'blue'}

def isDisjoint(item, item1):
    print(f'Is set1 is a disjoint of set2 : {item.isdisjoint(item1)}')

isDisjoint(set1, set2)
