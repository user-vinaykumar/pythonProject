# already practised problem for improvment.

def firstLetter(item):
    return item[0]

def arrangeList(lis):
    return sorted(lis, key=firstLetter)


print(arrangeList(['ariun', 'vinay', 'bharath']))
