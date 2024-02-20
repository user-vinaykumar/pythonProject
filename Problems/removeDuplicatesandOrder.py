# remove the duplicates from the list and maintain the order as it is given in the original list.

sheet = ['a', 'b', 'a', 'c', 'a', 'b']

def removeAndOrder(item):
    new = []
    for i in item:
        if i not in new:
            new.append(i)
        else:
            pass
    return new


print(removeAndOrder(sheet))


# second way of doing it.

def removePlusOrder(item):
    newlist = list(dict.fromkeys(sheet).keys())
    return newlist

print(removePlusOrder(sheet))