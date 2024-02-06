tup = (1, 2, ['a', 'b'], 3)

tup[2].append('c')  # even though tuples are immutable we can append with the values of the list present in the tuple.

print(tup)

tup[2].append(3)

print(tup)