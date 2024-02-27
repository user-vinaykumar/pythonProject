# print the item that is longer than the 'nth' charecters in the list.

laptops = ['dell', 'lenovo', 'hp', 'apple', 'samsung', 'htc', 'acer']

def problem(item, number):
    new = []
    for i in item:
        if len(i) > number:
            new.append(i)
        else:
            continue
    print(new)


problem(laptops, 2) # removes hp because hp is of length - 2.
problem(laptops, 3) # removes hp and htc because the length of these two is not > than 3
