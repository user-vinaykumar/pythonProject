number = [1,2,3,5,33,44,21,37,83,45,67,32,48]

# print the values inside number list is odd or even.

for num in number:
    if num % 2 == 0:
        print(f'{num} : Even!')
        continue
    elif num % 2 == 1:
        print(f'{num} : Odd!')
        continue
