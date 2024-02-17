# create a dictionary with firstname and lastname as keys and actual names as values
# and the dictionary as a name as nameDictionary.

nameDictionary = {}

def dictionary(item):
    item.update({'FirstName' : 'Vinay',
                                  'LastName' : 'Kumar'})
    return item

print(dictionary(nameDictionary))