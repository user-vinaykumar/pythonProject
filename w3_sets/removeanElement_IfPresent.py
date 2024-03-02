# remove an element from the set if the element present in the set.

sample = {1,3,4,5,6,7,8,9,76,544,33,32}

def removeIfPresent(item, element):
    if element in item:
        item.remove(element)
        print(f'the {element} element removed from the set and the set looks like this {item}.')
    else:
        print(f'Entered the wrong number. Enter the number which is in the set...!!!')


def solution(item1):
    number = int(input('Enter the number to be removed : '))
    removeIfPresent(item1, number)


solution(sample)