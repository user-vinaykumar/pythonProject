# given list = [2,1,+, 3, *]
# read 2 and 1 and apply addition after reading + read 3 and read * and
# multiply added number of 2 and 1 with 3. output would be 2+1 = 3 and 3*3 is 9

def apple(item):
    lists = []
    index = -1

    for i in item:
        if type(i) == int:
            lists.append(i)
            index += 1
        elif i == '+':
            lists.append(lists[-1] + lists[-2])
        elif i == '-':
            lists.append(lists[-1] - lists[-2])

        elif i == '*':
            lists.append(lists[-1] * lists[-2])
        elif i == '/':
            lists.append(lists[-1] / lists[-2])
        else:
            pass

    return lists[-1]


print(apple([1, 2, '+', 3, '*']))
