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

    def apply_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_amount))

    def __repr__(self):
        return self.fullname

    def __str__(self):
        return self.email

    def __add__(self, other):
        return self.pay + other.pay

class Developer(Employee):

    def __init__(self, firstname, lastname, pay, company, proglang):
        super().__init__(firstname, lastname, pay, company)
        self.proglang = proglang

