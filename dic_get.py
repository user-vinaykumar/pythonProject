student = {'name': 'vinay', 'age':26, 'subject':'CompSci'}

print(student.get('name'))  # prints the value of the key we provide in argument.

print(student.get('age'))

print(student.get('phone')) # passing the wrong key in .get() will return None

print(student['phone'])  # passing the wrong key w/o .get() will return KeyError

