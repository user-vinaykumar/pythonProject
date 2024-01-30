# string palindrome

str = input('Enter the string : ')


k = len(str)
j = 1
h = False
for i in range(0, round(k/2)):
    if(str[i]==str[-j]):
        h = True
        j+=1
    else:
        h=False


if(h==True):
    print('The given string is a palindrome..')
else:
    print('The given string is not a palindrome..')


