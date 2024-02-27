# remove even numbers from the list.

sampleList = [1,23,4,56,77,88,76,53,78,66,65,67,99]

def removeEven(item):
    output = []
    for i in item:
        if i%2 == 0:
            pass
        else:
            output.append(i)

    print(output)

removeEven(sampleList)
