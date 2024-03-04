# finds all the pair of numbers whose sum is equal to the given value.

list = [1,2,3,4,5,6,7,8,9,0]

value = 8

def test(item, target_val):
    checkList = []
    for i in item:
        j = target_val - i
        if j in item:
            checkList.append({i, j})
        else:
            pass

    print(f'the result of the following problem : {checkList}')


test(list, value)
