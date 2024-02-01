'''# list with 4 items should swap 2 and 4 positions

list = ['vinay', 'sharan', 'rajeshwari', 'shivalingaiah']
k = len(list)
str = ''
str2 = ''
str3 = ''
j = 0
k = 0

#list2 = ['', '', '', '']

for i in range(k):
    if(i==0):
        str = str + list[i + 1]

    elif(i==1):
        str2 = str2 + list[i + 2]

    else:
        print(' ')

str3 = str2 + ', ' + str

list2 = ', '.join(str3)

print(list2)'''



