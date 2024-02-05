# initialize dictionaries with default values.

employees = ['Kelly', 'Emma']
defaults = {'designation':'developer', 'salary':8000}

k = len(employees)

dict3 = {}

for i in range(k):
    dict3.update({employees[i]:defaults})


print(dict3)