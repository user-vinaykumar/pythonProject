# program to find even numbers from the list

list = [4,2,6,7,1,2,8,9]

list2 = []

k = len(list)
h = True
for i in list:
    if(i%2 == 0):       # i%2 == 1 for odd numbers.
        list2.append(i)
    else:
        h = False


print(list2)