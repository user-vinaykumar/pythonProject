list = ['vinay', 'sharan', 'rajeshwari', 'shivalingaiah']

list2 = []

k = len(list)

m = 1
print(list[k-m])
for i in range(k):
    list2.append(list[k-m])
    m+=1


print(list2)