# group the charecters based on their first letter.

from itertools import groupby

employee = ['sam', 'sarah', 'max', 'aria', 'mike', 'aaron']

employee.sort()

employee_group = groupby(employee, key= lambda n : n[0])

for key, group in employee_group:
    print(key, list(group))

