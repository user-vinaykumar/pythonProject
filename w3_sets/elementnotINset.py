# print the elements that are not in the other set.

sample = {'red', 'green', 'black', 'brown', 'purple', 'blue'}
colors = {'purple', 'green', 'orange', 'violet', 'maroon'}

def elementNotInOtherSet(item1, item2):
    return item1.difference(item2)

def solution(param1, param2):
    resultSet = elementNotInOtherSet(param1, param2)
    print(f'the set that has the result : {resultSet}')

solution(sample, colors)