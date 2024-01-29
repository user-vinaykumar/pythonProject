str = input('Enter the string : ')

str2 = ''

len = len(str)
k = 1

for i in range(len):
    str2 = str2 + str[len - k]
    k+= 1


print(str2)

