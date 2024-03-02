# create set difference.

sample = {1,2,3,4,5,6,7}
sample2 = {1,3,5,7}

def setDifference(item, item2):
    print(f'the difference of set : {item.difference(item2)}')

setDifference(sample, sample2)