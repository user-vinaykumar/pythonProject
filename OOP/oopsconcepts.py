class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.compnay = company

    raise_percent = 1.10

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.compnay}.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    def apply_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_percent))

    @classmethod
    def set_raise_percent(cls, percent):
        cls.raise_percent = percent

    @classmethod
    def emp_instance(cls, item):
        first, last, pay, comp = item.split(' ')
        return cls(first, last, pay, comp)

    def __repr__(self):
        return self.firstname

    def __str__(self):
        return self.lastname

    def __add__(self, other):
        return self.pay + other.pay

class Developer(Employee):

    def __init__(self, firstname, lastname, pay, company, proglang):
        super().__init__(firstname, lastname, pay, company)
        self.proglang = proglang

