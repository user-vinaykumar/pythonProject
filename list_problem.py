# swap two elements in a list

list = ['vinay', 'sharan']
list2 = ['', '']

k = len(list)
j = 1


for i in range(k):
    list2[i] = list[k-j]
    j+=1

print(list2)





