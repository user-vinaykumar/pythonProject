# convert a string to tuple.

stringchar = 'Python 3.0'

def stringToTuple(item):
    result = tuple(item)
    print(f'the string {item} is converted to tuple {result}')

stringToTuple(stringchar)