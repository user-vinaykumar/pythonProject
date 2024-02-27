# print the union of all the elements in a single list.


original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 5, 0]]

import itertools

value = list(itertools.chain(*original_list))
print(value)
