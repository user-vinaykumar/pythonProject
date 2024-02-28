# second largest in the list.

sample = [12,33,45,62,7,89,45,66,76]

def large(matter):
    largest = max(matter)
    return largest

def solution(item):
    item.remove(large(item))
    print(f'the second largest element in the list is : {large(item)}')

solution(sample)