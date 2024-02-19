'''# given an array of integers return true if the number of occurences of each value in the array
# is unique or false otherwise.

# integer = [1,1,2,2,2,3]
# output = True
# 1 has occured twice, 2 has occured thrice and 3 has occurred once. hence true.
import counter
def occurr(item):
    count = counter(item)
    print(count)
    #for i in item:

occurr([1,2])
'''


def occur(item):
    dictionary = {}
    sets = set()

    for i in item:
        dictionary[i] = dictionary.get(i, 0) + 1
    for value in dictionary.values():
        sets.add(value)
    if len(dictionary.values()) == len(sets):
        return True
    else:
        return False


print(occur([1, 2, 2, 1, 3]))