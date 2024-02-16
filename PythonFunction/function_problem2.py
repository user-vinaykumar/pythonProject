# write a function to multiply all of the elements in the list together and return a value
# the function has to work for lists, tuples and sets too.

def multiply(item):
    total = 1
    for i in item:
        total*=i
    return total

print(multiply([1,2,3,4,5,6]))
