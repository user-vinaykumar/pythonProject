class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    @property
    def fullname(self):
        return {f'{self.firstname} {self.lastname}'}

    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.company}.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

