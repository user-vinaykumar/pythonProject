# Inheritance concepts.

class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    raise_amount = 2.20

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

