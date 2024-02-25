# count the occurrence of an element.

lis = [1,2,3,4,5,6,3,4,2,3,3,3,5]

search = int(input('enter the number to be counted : '))

sets = set(lis)
count = 0

for i in lis:
    if i == 3:
        if search in sets:
            count+=1
        else:
            sets.add(i)


print(f'the number {search} appears {count} times.')

