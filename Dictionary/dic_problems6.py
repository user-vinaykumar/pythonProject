# remove some particular item and value from the list.

dictionary = {'Virat': 'Kohli',
              'Sachin': 'Tendulkar',
              'Harbajan': 'Singh',
              'Jorge': 'Lorenzo',
              'Casey': 'Stoner'}


def removeAnElement(item):
    del item['Jorge']
    return item


print(removeAnElement(dictionary))
