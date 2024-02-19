# swap variables a and b without using tuple unpacking.

a = 5
b = 8


def swap(j, k):
    print('the value of a :', j)
    print('the value of b :', k)
    g = j + k
    x = g - j
    y = g - k

    print('the value after swapping ----------------------------- :')
    print(f'the value of a is {x}')
    print(f'the value of b is {y}')


swap(a, b)
