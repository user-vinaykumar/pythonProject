# search an element in the list.

lis = [2,3,4,5,5,6,7,1,33,56]

search = int(input('Enter the number to be searched : '))


if search in lis:
    print(f'the number {search} found in the list.')
else:
    print(f'the number {search} is not found in the list.')


