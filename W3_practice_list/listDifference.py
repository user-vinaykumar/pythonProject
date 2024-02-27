# print the difference of two lists.


list1 = [1,3,5,7,9]
list2 = [1,2,4,6,7,8]

def inserting(object1, object2, object3):
    result = []
    for i in object1:
        if i in object3:
            pass
        else:
            result.append(i)

    for i in object2:
        if i in object3:
            pass
        else:
            result.append(i)

    return result





def commonElements(data1, data2):
    return data1.intersection(data2)

def main(item1, item2):
    set1 = set(item1)
    set2 = set(item2)
    commonvalues = commonElements(set1, set2)
    finalResult = inserting(item1, item2, commonvalues)
    print(finalResult)


main(list1, list2)


