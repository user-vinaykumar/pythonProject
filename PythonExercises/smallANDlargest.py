# find the smallest and largest number in a list.

lis = [1,23,45,66,7,3,8,34]

print(f'the smallest number in the list is {min(lis)}')
print(f'the largest number in the list is {max(lis)}')



print('---------------')
largest = 0
for i in lis:
    if i>largest:
        largest = i
    else:
        continue

print(f'the largest number in a list is {largest}')


for i in lis:
    smallest = lis[0]
    if i > smallest:
        pass
    else:
        smallest = i


print(f'the smallest number in a list is {smallest}')

