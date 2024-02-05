# program to create a new dictionary by extracting the mentioned keys from the below dictionary

dic = {'name':'vinay', 'age':27, 'salary':8000, 'city':'mandya'}

k = ['name', 'salary']

dic2 = {}

for i in k:
    dic2.update({i:dic[i]})

print(dic2)




# other ways to do the same thing

dic = {'name':'vinay', 'age':27, 'salary':8000, 'city':'mandya'}
keys = ['name', 'salary']

di = dict()

di = {k : dic[k] for k in keys}
print(di)

