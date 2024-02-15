# remove the duplicates in the list in a single line of code.

list3 = [1,2,3,4,5,3,42,5,6,2,9]

new_list = list(dict.fromkeys(list3))

print(new_list)

