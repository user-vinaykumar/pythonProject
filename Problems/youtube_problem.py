# given a string return the first letter that is repeated twice.

string = 'letter'

def function(item):
    s = set()
    j = 0
    for i in item:
        s.add(i)
        j+=1
        if j > len(s):
            return i
        else:
            pass

print(function('google'))




def alternative(item):
    newlist = []
    for i in item:
        if i in newlist:
            return i
        else:
            newlist.append(i)

print(alternative('google'))