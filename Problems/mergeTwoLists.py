# merge two lists and remove duplicates

list1 = [1,2,3,3,4,5,6]
list2 = [4,4,5,6,7,8,9]

def mergeLists(item1, item2):
    set1 = set(item1)
    set2 = set(item2)
    sets = set1.union(set2)
    return sets

print(mergeLists(list1, list2))