# check whether the lists are circularly identical.

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 10]

print('compare list1 and list2')
print(' '.join(map(str, list1)))

print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('compare list1 and list3')
print(''.join(map(str, list3)) in ''.join(map(str, list1 * 2)))


