# move the first item of list to the last element. or move it to any specific index.

inv = ['gem', 'sword', 'shield', 'potion']

def funct(item):
    length = len(inv)
    indx = inv.index(item)

    inv.insert(length-1, inv.pop(indx))
    return inv

print(funct('sword'))

print('ffffffffffffffffffffffffffffff')

# move 'gem' to the end of the list

def move(item):
    indx = inv.index('gem')
    inv.append(inv.pop(indx))
    return item


print(move(inv))
