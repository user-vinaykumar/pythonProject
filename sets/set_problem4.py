# remove an element from a set.

sets = {'a', 'vinay', 4, 'sharan'}
sets2 = tuple(sets)

sets.remove('a')  # remove will remove particular item, and pop will remove the last item.

print(sets)

sets3 = set(sets2)

sets3.discard('sharan')
print(sets3)
