# creating the class of the python.

class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

print(emp_2)
print(emp_1)

emp_1.first = 'vinay'
emp_1.last = 'kumar'
emp_1.email = 'vinay.kumar@company.com'
emp_1.pay = 50000

emp_2.first = 'sharan'
emp_2.last = 'gs'
emp_2.email = 'sharan.gs@gmail.com'
emp_2.pay = 70000

print(emp_2.first)

print(emp_1.pay)