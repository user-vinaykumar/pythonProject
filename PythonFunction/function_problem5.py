# program to take the list and returning another list whose elements are the values of the
# first list squared.

def squareMachine(item):
    newList = []
    for i in item:
        j = i * i
        newList.append(j)
    return newList


print(squareMachine([1, 2, 3, 4, 5]))
