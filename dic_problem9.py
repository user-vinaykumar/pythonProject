# rename the key city to location.

dic = {'name': 'vinay', 'age': 27, 'salary': 8000, 'city': 'mandya'}

dic['location'] = dic.pop('city')

print(dic)
