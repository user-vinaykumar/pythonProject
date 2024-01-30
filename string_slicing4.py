# Accept a string from user and display the string with each charecter of the
# word in caps

str = input('Enter the string : ')

str2 = ''

L = str.split()



for i in L:
    str2 = str2 + i[0].upper() +i[1:] + ' '

print(str2)


