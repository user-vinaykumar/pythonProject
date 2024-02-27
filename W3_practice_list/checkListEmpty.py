# check whether the list is empty or not

cities = ['mandya', 'mysuru', 'chamarajanagara', 'hassana', 'kolara']

def checklistEmpty(item):
    for i in item:
        if i not in item:
            return 'the list is empty.'
        else:
            return 'the list is not empty.'


print(checklistEmpty(cities))


# second approach

def emptycheck(item):
    k = len(item)
    if k == 0:
        return 'the list is empty.'
    else:
        return 'the list is not empty.'


print(emptycheck(cities))