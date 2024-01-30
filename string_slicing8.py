# accept a string from the user and display first two charecters of each word.

str = input('Enter the string : ')

k = len(str)

str2 = ''

l = str.split()

for i in l:
    str2 = str2 + i[0:2] + ' '


print(str2)