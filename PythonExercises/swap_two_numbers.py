num1 = input('Enter the num1 : ')
num2 = input('Enter the num2 : ')

print(f'num 1 before swapping : {num1}')
print(f'num 2 before swapping : {num2}')
print('---------')

num1, num2 = num2, num1  # tuple unpacking method

print(f'num1 after swapping : {num1}')
print(f'num2 after swapping : {num2}')

print('------------')

# approach 2

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

print('--------------')

# approach 3

value1 = input('Enter the value1 : ')
value2 = input('Enter the value2 : ')

print(f'the value1 before swapping : {value1}')
print(f'the value2 before swapping : {value2}')

print('----------------')  # by variable1.replace(variable1, variable2) same goes
# for variable2.   example given down below.

print(f'the value1 after swapping : ', value1.replace(value1, value2))
print(f'the value2 after swapping : ', value2.replace(value2, value1))
