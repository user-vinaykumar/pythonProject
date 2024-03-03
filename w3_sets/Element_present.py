# check whether or not element present in a set.

set1 = {'red', 'green', 'black', 'blue', 'yellow', 'purple', 'pink', 'white'}

def checkElementInSet(item, element):
    if element in item:
        print(f'the element {element} is present in the set {item}')
    else:
        print(f'the element {element} is not present in the set {item}')

checkElementInSet(set1, 'green')