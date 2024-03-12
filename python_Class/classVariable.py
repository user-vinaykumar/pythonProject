# difference in class variable and instance variable.

class Employee:
    total_num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, firstName, lastName, pay, email, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = email
        self.phone = phone

        Employee.total_num_of_emps +=1


    def fullName(self):
        return f'full name of the employee is {self.firstName} {self.lastName}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.total_num_of_emps) # value will be 0 because no instance is created.
print(f'--------------------')
emp1 = Employee('vinay', 'kumar', 60000,
                'vinaykumar@gmail.com', 78990978)

emp2 = Employee('sharan', 'gs', 50000,
                'sharangs@gmail.com', 733952)

# emp2.raise_amount = 1.05  only alters the emp2 raise amount attribute.
# print(emp2.__dict__)
#

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.total_num_of_emps)  # the value is 2 since two instances are created and
                                    # total_num_of_two variable is incremented twice because of
                                    # we instantiated emp1 and emp2 of Employee twice.


# print(emp2.__dict__)
# print(emp1.__dict__)
# print(Employee.__dict__)