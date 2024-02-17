# generate a list of values of a dictionary in a new list.

dictionary = {'Karnataka': 'Bengaluru',
              'Kerala': 'Thiruvananthapura',
              'Telangana': 'Hyderabad',
              'Odissa': 'Bhubaneshwara'}


def valuefun(item):
    valueList = list(item.values())
    return valueList


print(valuefun(dictionary))
