# smallest element in a list.

mall = [2,3,44,5,1,6,7,0,77,32,34,57]

def smallest(item):
    small = item[0]
    for i in item:
        if i<small:
            small = i
        else:
            continue

    print(f'the smallest element in the list {item} is : {small}')

smallest(mall)
