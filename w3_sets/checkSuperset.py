# check whether the given set is a superset of itself and superset of other set.

sample = {'red', 'green', 'orange', 'blue', 'brown', 'black', 'white'}
grace = {'orange', 'blue', 'brown'}
color = {'geeen', 'maroon'}

def checkSuperset(item1, item2):
    return item1.issuperset(item2)

def checkSupersetItself(item):
    return item.issuperset(item)

def solution(item11, item22, item33):
    print(f'the set1 is a superset of itself : {checkSupersetItself(item11)}')

    print(f'the set1 is a superset of set2 : {checkSuperset(item11, item22)}')

    print(f'the set1 is a superset of set3 : {checkSuperset(item11, item33)}')

solution(sample, grace, color)