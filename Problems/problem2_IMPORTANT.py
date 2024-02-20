# merge two dictionaries if same key value pair appears then the value must be added.

inv = {'sword' : 1,
       'potion' : 3}

loot = {'sword' : 1,
        'potion' : 2,
        'shield' : 1}

# need to merge these two dictionaries


def mergeTwoDictionaries(item, wood):
    set1 = set(item)
    set2 = set(wood)
    set3 = set1.union(set2)
    newlist = {k : item.get(k, 0) + wood.get(k, 0) for k in set3}
    return newlist

print(mergeTwoDictionaries(inv, loot))

#new = {k : inv.get(k, 0)} + loot.get(k, 0) for k in set(inv )