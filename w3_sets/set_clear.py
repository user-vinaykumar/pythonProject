# remove all elements from the set.

set1 = {'red', 'green', 'purple', 'black'}

def clearSet(item):
    item.clear()
    print(f'the set is clear now : {item}')

clearSet(set1)