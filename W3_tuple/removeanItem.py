# remove an item from the tuple

mall = (1,3,4,5,6,7,8)

def removeTupleElement(item, element):
    indx = item.index(element)
    one = item[:indx]
    two = item[indx+1 : ]
    print(f'the tuple {item} after removal of the {element} :- {one + two}')

removeTupleElement(mall, 4)