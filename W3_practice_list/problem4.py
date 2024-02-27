# Write a Python program to print a specified list after removing
# the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

sampleList = ['red', 'green', 'white', 'black', 'pink', 'yellow']


def pro(item):
    output = []
    for i in item:
        k = item.index(i)
        if k == 0:
            pass
        elif k == 4:
            pass
        elif k == 5:
            pass
        else:
            output.append(i)

    print(item, output)

pro(sampleList)