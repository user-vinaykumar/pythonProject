# check all the elements in the list are prime numbers.
# if all the elements are prime numbers then return true or else false.

list1 = [0, 3, 4, 7, 9]
list2 = [3, 5, 7, 13]
list3 = [1, 5, 3]


def primeResult(numb):
    if numb >= 1:
        return False  # the number is not prime.
    else:
        return True  # the number is prime.


def primeCheck(num):
    count = 0
    if num > 1:
        for numbers in range(2, num):
            if num % numbers == 0:
                count += 1
            else:
                continue
    else:
        count = 3

    return count


def isListPrime(item):
    total = 0
    for i in item:
        value = primeResult(primeCheck(i))
        if value == True:
            total += 1
        else:
            continue
    return total


def result(items):
    if len(items) == isListPrime(items):
        print(f'the List {items} is : True')
    else:
        print(f'the list {items} is : False')


result(list3)
