# count the elements in a list within a specified range.

sample = [1,2,3,4,49,45,46,57,56,58,59,6,78,89,98,65,58,44]

def count(item):
    value = 0
    for i in item:
        if i in range(40, 100):
            value+=1
        else:
            pass
    return value

def solution(matter):
    print(f'Element count in the range of 40 and 100 is : {count(matter)}')

solution(sample)
