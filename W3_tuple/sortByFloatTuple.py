# sort the tuples in a lists by their floar value.

sample = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

def sort(n):
    return n[-1]

def sortByFloat(item):
    sortedValue = sorted(item, key=sort)
    print(sortedValue)

sortByFloat(sample)