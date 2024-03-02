# convert the string literals to integer for the elements in the tuple.

sample = (('333', '33'), ('1416', '55'))

def stringToInt(item):
    result = tuple((int(x[0]), int(x[1])) for x in item)
    print(f'the string tuple {item} is converted to integer : {result}')

stringToInt(sample)