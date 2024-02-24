num1 = input('Enter the num1 : ')
num2 = input('Enter the num2 : ')

print(f'num 1 before swapping : {num1}')
print(f'num 2 before swapping : {num2}')
print('---------')

num1, num2 = num2, num1  # tuple unpacking method

print(f'num1 after swapping : {num1}')
print(f'num2 after swapping : {num2}')

print('------------')

number1: int = 20
number2: int = 30

print(f'number1 before swapping is : {number1}')
print(f'number2 before swapping is : {number2}')
print('---------------')

sum: int = number1 + number2

number1 = sum - number1
number2 = sum - number2

print(f'number1 after swapping is : {number1}')
print(f'number2 after swapping is : {number2}')
