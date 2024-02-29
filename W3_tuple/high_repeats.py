# print the element that got repeated more times in a list.

sample = (1,2,3,4,5,1,1,1,6,1,7,1)

def reverseDic(thing):
    newDictionary = {i : j for j, i in thing.items()}
    return newDictionary

def dicFun(n, itemdic):
    itemdic[n] = itemdic.get(n, 0)+1
    return itemdic

def solution(item):
    dictionary = {}
    for i in item:
        resultDic = dicFun(i, dictionary)
    maxvalue = max(list(resultDic.values()))
    reversedDictionary = reverseDic(resultDic)

    print(f'the number {reversedDictionary[maxvalue]} repeated {maxvalue} times')


solution(sample)





