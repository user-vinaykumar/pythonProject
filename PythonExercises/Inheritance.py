class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    raise_amount = 1.10

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def emp_instance(cls, item):
        first, last, pay, comp = item.split(' ')
        return cls(first, last, pay, comp)

    def apply_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_amount))

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

    def __repr__(self):
        return f'{self.fullname}'

    def __add__(self, other):
        return self.pay + other.pay

    def __str__(self):
        return self.email

    @property
    def pay(self):
        return self.pay

    @pay.setter
    def pay(self, sal):
        self.pay = sal

    @property
    def company(self):
        return self.company

    @company.setter
    def company(self, com):
        self.company = com

class Developer(Employee):

    def __init__(self, firstname, lastname, pay, company, proglang):
        super().__init__(firstname, lastname, pay, company)
        self.proglang = proglang

class Manager(Employee):

    def __init__(self, firstname, lastname, pay, company, employees=None):
        super().__init__(firstname, lastname, pay, company)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            list.append(emp)
        else:
            pass

    def remove_emp(self, emp):
        if emp in self.employees:
            list.remove(emp)
        else:
            pass

