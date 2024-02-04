# updating the dic with .get() method
student = {'name':'vinay', 'age':25, 'subject':'Math'}

print(student.get('phone')) # passing the wrong key in .get() will return None

# updating the dic key with .get() method but it will not update the initial dic

print(student.get('phone', 'Not Found'))  # updating phone key with NotFound value
print(student.get('phone', '7899097827')) # updating phone key with phone_number

print(student.get('brother', 'sharan'))
print(student)

