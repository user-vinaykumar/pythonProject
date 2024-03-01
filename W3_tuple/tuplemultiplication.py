# multiply all the elements in the tuple.

sample = (4, 3, 2, 2, -1, 18)

def multiplyTupleElement(item):
    count = 1
    for i in item:
        count*=i
    print(f'the value after multiplying all the elements : {count}')

multiplyTupleElement(sample)