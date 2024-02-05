# convert two lists into a dictionary using update method

keys = ['vinay', 'sharan', 'rajeshwari', 'shivalingaiah']

value = [0, 1, 2, 3]
j = len(keys)

dic2 = {}

for i in range(j):
    dic2.update({value[i]: keys[i]})

print(dic2)
