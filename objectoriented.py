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

    raise_percent = 1.10

    @classmethod
    def set_raise_percent(cls, percent):
        cls.raise_percent = percent

    @classmethod
    def emp_instance(cls, item):
        first, last, pay, comp = item.split(' ')
        return cls(first, last, pay, comp)

    def apply_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_percent))

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

class Manager(Employee):

    def __init__(self, firstname, lastname, pay, company, employeelist=None):
        super().__init__(firstname, lastname, pay, company)
        if employeelist is None:
            self.employeelist = []
        else:
            self.employeelist = employeelist

    def add_emp(self, emp):
        if emp not in self.employeelist:
            self.employeelist.append(emp)
        else:
            pass

    def remove_emp(self, emp):
        if emp in self.employeelist:
            self.employeelist.remove(emp)
        else:
            pass

    def print_emp(self):
        for emp in self.employeelist:
            print(f'--> {emp.fullname}')

