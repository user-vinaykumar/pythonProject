# inheritance concepts revised.

class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

