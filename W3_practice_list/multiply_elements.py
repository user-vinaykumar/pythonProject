# multiply all the elements in a list.

mall = [1,3,4,5,6]

def multiplyElements(item):
    value = 1
    for i in item:
        value*=i
    print(f'the total multiplication value of the list {item} is : {value}')

multiplyElements(mall)