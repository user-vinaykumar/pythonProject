# prime numbers in a range of numbers.

prime = [i for i in range(2, 100) if 0 not in [i%n for n in range(2, i)]]

print(prime)