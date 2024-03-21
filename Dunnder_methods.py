# Concepts of Dunnder methods.

class Employee:
    raise_amount = 1.10
    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    def fullname(self):
        return f'full name : {self.firstname} {self.lastname}'

    def email(self):
        return f'email : {self.firstname}.{self.lastname}@{self.company}.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

