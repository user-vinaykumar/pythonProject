#sum of all the elements in a list.


mall = [3,4,2,7,5,8]

def sumOfAllElements(item):
    count = 0
    for i in item:
        count+=i
    print(f'the sum of elements of the list {mall} is : {count}')

sumOfAllElements(mall)
