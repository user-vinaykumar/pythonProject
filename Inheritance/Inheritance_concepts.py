# Inheritance concepts - applying everything I learnt till now.

class Employee:

    raise_amount = 1.10

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amount = amount

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


