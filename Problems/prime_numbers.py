# prime numbers in a range of numbers.

prime = [i for i in range(2, 100) if 0 not in [i%n for n in range(2, i)]]

print(prime)


def isPrime(item):
    primeList = [i for i in item if 0 not in [i%n for n in range(2, i)]]
    print(primeList)

isPrime([2,777,33,41,29,22,999,33])