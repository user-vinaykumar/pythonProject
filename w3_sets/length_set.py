# print the length of a set.

set1 = {'red', 'green', 'purple', 'black', 'brown', 'blue', 'grey', 'yellow', 'pink', 'white'}

def setLength(item):
    count = 0
    for i in item:
        count+=1
    print(f'the length of the {item} is : {count}')

setLength(set1)