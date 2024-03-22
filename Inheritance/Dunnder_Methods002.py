# dunnder methods part 2

class Employee:

    raise_amount = 1.10

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    def fullname(self):
        return f'full name : {self.firstname} {self.lastname}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.amount = amount

class Developer(Employee):

    def __init__(self, firstname, lastname, pay, company, proglang):
        super().__init__(firstname, lastname, pay, company)
        self.proglang = proglang


    def programming(self):
        return f'language he is performing : {self.proglang}'

class Manager(Employee):

    def __init__(self, firstname, lastname, pay, company, employees=None):
        super().__init__(firstname, lastname, pay, company)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            pass




