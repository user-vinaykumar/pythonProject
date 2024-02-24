num = int(input('Enter the number : '))

count = 0
for i in range(1, num):
    if num%i == 0:
        count+=1
    else:
        pass
if count == 1:
    print(f'the given number {num} is a prime number.')
else:
    print(f'the given number {num} is not a prime number.')