# generate a list of keys from a dictionary and store it in a list.

dictionary = {'Vinay': 'Gixxer SF 250',
              'Sharan': 'Xpulse 200',
              'Suhas': 'KTM Duke 200'}


def keysOfDictionary(item):
    keysList = list(dictionary.keys())
    return keysList


print(keysOfDictionary(dictionary))
