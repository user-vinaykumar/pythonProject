# arrange the dictionary with its keys in alphabetical order.

dictionary = {'Aman' : 22, 'Chethan' : 35, 'Zabi' : 33, 'Rahul' : 23, 'Manu' : 21}

sorted_dictionary = sorted(dictionary.keys())

for key in sorted_dictionary:
    print(key, dictionary[key])