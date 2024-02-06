# program to check whether a list contains a duplicate elements.

list2 = [0,0,3,4,2,7,8]

unique_values = list(set(list2))

if len(unique_values)==len(list2):
    print('The given list does not contain duplicate values...')
else:
    print('The given list do contain duplicate elements...')

