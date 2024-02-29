# find the index of the element in a tuple

mall = (1,3,4,5,6,7,44,32,2)

def tupleIndexFinder(item, element):
    count = 0
    for i in item:
        if i == element:
            print(f'the index of the {element} is : {count}')
            count+=1
            break
        else:
            count+=1

tupleIndexFinder(mall, 5)
print('-------------------------')
tupleIndexFinder(mall, 44)