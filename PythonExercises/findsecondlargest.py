# find the second largest number in a list.

lis = [1,2,44,55,63,21,88,44,23]

def largest(item):
    count = 0
    for i in item:
        if i > count:
            count = i
        else:
            continue
    return count


print(largest(lis))
lis.remove(largest(lis))

print(f'the second largest element in the list is {largest(lis)}')

