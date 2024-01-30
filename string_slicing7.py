str = input('Enter the string : ')

n = int(input('Enter the number of charecters to be extracted from the right : '))

k = len(str)

if(n>k):
    print('Enter less number!')

else:
    print(str[k-n:])

