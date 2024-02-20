# move the first item of list to the last element. or move it to any specific index.

inv = ['gem', 'sword', 'shield', 'potion']


# move 'gem' to the end of the list

def move(item):
    item.append(item.pop(0))
    return item


print(move(inv))
