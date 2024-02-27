# clone a list or copy a list.

brands = ['nike', 'adidas', 'reebok', 'sketchers', 'puma', 'asian']


# first approach

def clonealist(item):
    cloned = item
    print(cloned)

clonealist(brands)


# second approach

def copyaList(item):
    copied = item[::-1]
    copied = copied[::-1]

    print(copied)

copyaList(brands)