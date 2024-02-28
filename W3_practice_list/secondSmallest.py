# print the second smallest number in a list.

sample = [3,5,6,33,42,7,8,9,89]

def small(item):
    smallest = min(sample)
    return smallest

def solution(item):
    small(item)
    item.remove(small(item))
    print(f'the second smallest element in the list is : {small(item)}')

solution(sample)