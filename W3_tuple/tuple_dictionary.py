# convert the tuple to dictionary.

sample = ((6888, 'vinay'), (77778444, 'sharan'))

def tupleToDictionary(item):
    tupledic = dict((x, y) for y, x in item)
    print(f'the tuple {item} converted to dictionary : {tupledic}')

tupleToDictionary(sample)