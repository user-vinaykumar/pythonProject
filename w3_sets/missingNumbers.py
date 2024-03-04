# Find the missing numbers of the corresponding sets.

sample1 = {1,2,3,4,5,6,7,8}
sample2 = {3,4,5,6,7,8,9,0}

def difference(item1, item2):
    return item1.difference(item2)

def solution(items1, items2):
    print(f'missing numbers in second set as compared '
          f'to first set : {difference(items1, items2)}')

    print(f'missing numbers in first set as compared '
          f'to second set : {difference(items2, items1)}')

solution(sample1, sample2)