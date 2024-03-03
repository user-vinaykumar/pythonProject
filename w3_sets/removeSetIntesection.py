# remove the intersection of the sets.

sample1 = {1,2,3,4,5,6,7}
sample2 = {5,6,7,8,9,10}

def removeCommonElements(item1, item2):
    result = set()
    for i in item1.union(item2):
        if i in item1.intersection(item2):
            pass
        else:
            result.add(i)

    print(f'the set after removing the elements from the intersection of two sets... : {result}')

removeCommonElements(sample1, sample2)