# print true if a list contains a subset in it.

sample = [2,4,3,5,7]
sub1 = [4,3]
sub2 = [3, 7]

def indx(num, lis):
    return lis.index(num)

def sol2(ite1, ite2, coun):
    if coun < len(ite2):
        if ite2[coun] in ite1:
            inx = indx(ite1[coun], ite1)
        else:
            pass

    return inx

def sol(item1, item2):
    count = 0
    for i in item2:
        if count < len(item2):
            one = sol2(item1, item2, count)
            count+=1
        else:
            pass
