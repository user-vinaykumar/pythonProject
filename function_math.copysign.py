import math

def copysign(num1, num2):
    print(num1, num2)
    return math.copysign(num1, num2)

print(copysign(4, -9))  # returns num1 with the sign of num2.