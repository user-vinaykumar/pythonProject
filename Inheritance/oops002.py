class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.company}.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    raise_amount = 1.10

    def apply_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_amount))

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def emp_isntance(cls, item):
        first, last, pay, company = item.split(' ')
        return cls(first, last, pay, company)

class Developer(Employee):

    def __init__(self, firstname, lastname, pay, company, proglang):
        super().__init__(firstname, lastname, pay, company)
        self.proglang = proglang

class Manager(Employee):

    def __init__(self, firstname, lastname, pay, company, employeeslist=None):
        super().__init__(firstname, lastname, pay, company)
        if employeeslist is None:
            self.employeeslist = []
        else:
            self.employeeslist = employeeslist

