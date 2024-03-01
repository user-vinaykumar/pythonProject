# find the length of the tuple.

sample = (11,44,54,66,7,54,32,12)

def tupleLength(item):
    count = 0
    for i in item:
        count+=1
    print(f'the length of the tuple is : {count}')


tupleLength(sample)