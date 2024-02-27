# print the index and value of the list

list1 = [1,2,4,5,7,8,9,4]

def indexANDvalue(item):
    for indx, value in enumerate(item):
        print(indx, value)

indexANDvalue(list1)