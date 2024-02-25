# find the factorial of a number.


num = int(input('Enter the number : '))
m = 1
if num<0:
    print(f'the factorial is not there for negative number.')
elif num==0:
    print(f'the factorial of {num} is : 1')
else:
    for i in range(1, num + 1):
        m *= i
    print(f'the factorial of the given number {num} is : {m}')