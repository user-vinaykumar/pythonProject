# write a python program to find the common prefix to all the strings in a list.

# [pqrvinay, pqrsharan, pqrrajeshwari]  ==> pqr is the common prefix.

sample = ['pqrvinay', 'pqrsharan', 'pqrrajeshwari']




# def minword(item):
#     return min(item, key=len)

def setsofword(items):
    minlength = min([len(word) for word in items])
    for i in range(minlength):
        chars = set([word[i] for word in items])
        if len(chars)>1:
            print(f'the common prefix for all the words in the list : {items[0][:i]}')
            break
        else:
            pass

setsofword(sample)






# def minItem(item):
#     minLen = min(item, key=item.count)
#     print(minLen)
#     return len(minLen)
#
# minItem(sample)



