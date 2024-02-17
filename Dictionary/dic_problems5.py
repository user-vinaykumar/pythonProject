# remove all the elements from the dictionary

dictionary = {'Asia': 'India',
              'Europe': 'Spain',
              'Australia': 'New Zeland'}


def removeElements(item):
    item.clear()
    print(f'_{item}_ is Empty!')


removeElements(dictionary)
