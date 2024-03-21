# Inheritance concept covering.

class Employee:
    raise_amount = 1.10
    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.last = lastname
        self.pay = pay
        self.company = company

    def fullname(self):
        return f'full name : {self.firstname} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def email(self):
        return f'email : {self.firstname}.{self.last}@{self.company}.com'

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount



