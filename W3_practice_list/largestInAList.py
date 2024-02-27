# largest number in a list.

mall = [2,5,3,8,3,99,44,21]

def largest(item):
    large = 0
    for i in item:
        if i>large:
            large = i
        else:
            continue
    print(f'the largest number in a list {item} is : {large}')

largest(mall)