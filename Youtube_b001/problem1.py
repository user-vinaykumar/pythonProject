# move first element of the list into the last.

sheet = ['gem', 'sword', 'potion', 'chisel']


def fun(item):
    tools = list(sheet)
    length = len(tools)
    ind = tools.index(item)

    tools.insert(length - 1, tools.pop(ind))
    return tools


print(fun('gem'))
print(fun('sword'))
print(sheet)
