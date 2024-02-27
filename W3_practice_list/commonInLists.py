# write a fun that takes two lists and returns true if at least
# one element is common

cities = ['mandya', 'mysuru', 'bengaluru', 'tumakuru', 'hassana']

capitals = ['chennai', 'hyderabad', 'bengaluru', 'kochi', 'vijayawada']

def checkCommonInTwoLists(item, item2):
    for i in item:
        if i in item2:
            return False
        else:
            return True


print(checkCommonInTwoLists(capitals, cities))