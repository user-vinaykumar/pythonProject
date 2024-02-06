a = [1,2,3]
b = [1,2,3]

print(a==b)   # equates the two lists

print(a is b)  # does not belong to same memory location. both are different objects.

print(id(a))
print(id(b))

a1 = [2,3,4]
b1 = a1

print(id(a1))
print(id(b1))

print(a1 == b1)