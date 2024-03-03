# check the set is superset of itself.

set1 = {1,2,3,4,5,6,7,8}

def issuperset_check(item):
    print(f'the {item} is superset of itself : {item.issuperset(item)}')

issuperset_check(set1)


print('----------------------------')

# check whether the set1 is superset of other sets.

sample1 = {'red', 'black', 'green', 'yellow', 'pink'}
sample2 = {'red', 'pink'}
sample3 = {'black', 'orange'}

def checkSuperset(item1, item2):
    print(f'Is {item1} is superset of {item2} : {item1.issuperset(item2)}')

checkSuperset(sample1, sample3)