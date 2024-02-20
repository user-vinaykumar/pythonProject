# find the element that got repeated more.

sheet = [100,2,100,3,4,100,2,4,100]

def countrepeat(item):
    dictionary = {}
    for i in item:
        dictionary[i] = dictionary.get(i, 0)+1
    indx = max(dictionary.values())
    newDictionary = {k : j for j, k in dictionary.items()}
    return newDictionary[indx]


print(countrepeat(sheet))

# second way of doing this

x = [1,2,1,3,4,1,2,4,1]
#print(x.count(1))

most = max(x, key=x.count)
print(most)






