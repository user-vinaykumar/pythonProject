# corey schafer python oops.

class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    @property
    def fullname(self):
        return f'full name : {self.firstname} {self.lastname}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    @property
    def email(self):
        return (f'email of the employee is : {self.firstname}{self.lastname}'
                f'@{self.company}.com')


