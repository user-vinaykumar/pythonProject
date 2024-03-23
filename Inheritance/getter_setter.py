# inheritance concepts with getter and setters.

class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company
    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.company}.com'

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

emp1 = Employee('vinay', 'kumar', 89999, 'virtusa')
print(emp1.fullname)
emp1.fullname = 'sharan gs'
print(emp1.fullname)
print(emp1.email)
emp1.fullname = 'vinay kumar'
print(emp1.email)
# emp1.email = 'spoorthi@gmail.com'
# print(emp1.email)
