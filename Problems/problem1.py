# print the list that has last names of each person provided in its first list.


def sub(lis):
    last = [n.split(' ')[-1] for n in lis]

    print(last)


sub(['vinay kumar', 'arun jamal', 'john cena'])
