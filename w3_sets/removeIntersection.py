# remove intersected elements from the set.

sample = {1,2,3,4,5,6,7,8}
sample2 = {4,5,6,9,0}

def intersectionElements(item1, item2):
    return item1.intersection(item2)

def validateIntersectElements(thing, sets, intset):
    for i in thing:
        if i in intset:
            pass
        else:
            sets.add(i)

    return sets

def solution(item11, item22):
    intersectResult = intersectionElements(item11, item22)
    resultSet = set()
    print(f'the output of the following problem : '
          f'{validateIntersectElements(item11, resultSet, intersectResult)}')


solution(sample, sample2)


