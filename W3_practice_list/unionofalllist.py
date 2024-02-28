# print the union of all the elements in a single list.


original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 5, 0]]

import itertools

value = list(itertools.chain(*original_list))
print(value)


second_list = [[1,2,3], [4,5,6], [7,8]]

flattened_list = list(itertools.chain(*second_list))
print(flattened_list)
