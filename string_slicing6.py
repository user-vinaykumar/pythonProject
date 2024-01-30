str = input('Enter the string : ')

n = int(input('Enter the number of charecters to be extracted from the left : '))

k = len(str)

if(n>k):
    print('Enter less number!')

else:
    print(str[0:n])

