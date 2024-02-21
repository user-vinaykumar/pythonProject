print('Imported the module...........')

variable = 'my_variable'


def indexfinder(item, value):
    for index, element in enumerate(item):
        if element == value:
            return index
    return -1
