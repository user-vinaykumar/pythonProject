# program to check if the given list is in ascending or not

list = [1,2,3,4,5,2,7]

k = len(list)
j =0
h = False
for i in range(k):
    if(j<=k-2):
        if(list[j]<list[j+1]):
            j+=1
            h = True
        else:
            h = False

if(h==True):
    print('The given list is in ascending order.')
else:
    print('The given list is not in ascending order.')