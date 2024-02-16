# write a python function called max_of_three to find the maximum value between three
# numbers and do not use the max() function that is pre built already.

def max_of_two(x, y):
    if x > y:
        return x
    return y

def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))

print(max_of_three(4,999,90))
