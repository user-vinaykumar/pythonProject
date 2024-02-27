# write a python program to generate and print a list of the first and last
# 5 elements where the values are square numbers between 1 and 30.

def fun():
    squareList = []
    for i in range(1, 30):
        squareValue = i * i
        squareList.append(squareValue)
    print(squareList[:5])
    print(squareList[-5:])

fun()