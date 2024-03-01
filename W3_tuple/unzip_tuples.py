# unzip the tuples to form a lists.

sample = ((3, 4), (3, 9), (2, 6), (4, 6))

result = list(zip(*sample))  # while unzipped the first element of the tuple will be listed
# as one list and the second element as second list.
# only if the all the tuples contain same number of elements.


print(f'the {sample} tuples unzipped : {result}')
