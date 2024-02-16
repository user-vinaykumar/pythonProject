# write a program that takes dictionary as an input and prints two lines of code that is
# one line with keys of dictionary and another line with values.

def dicDecomposer(item):
    keyList = []
    valueList = []
    for i in item:
        keyList.append(i)

    print(f'Keys of the dictionary are : {keyList}')

    newDictionary = {j : k for k, j in item.items()}

    for y in newDictionary:
        valueList.append(y)

    print(f'Values of dictionary are : {valueList}')


dicDecomposer({'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4})





