# clone the list

lis = [1,2,3,4,5,6]

new = [i for i in lis]

print(new)


print('----------------')

lis = [4,3,2,1,0,-1,-2,-3,-4]

newlis = lis[::-1]
finallis = newlis[::-1]
print(finallis)

print('-------------------')



alis = [1,4,6,7,0]

fina = alis.copy()
print(fina)
