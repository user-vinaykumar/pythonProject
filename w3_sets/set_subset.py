# check whether the set is a subset of another.

sample = {'mango', 'apple', 'orange', 'grapes'}
sample2 = {'apple', 'grapes'}

def subset(item, item2):
    print(item2.issubset(item))

subset(sample, sample2)