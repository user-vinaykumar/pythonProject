class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.last = lastname
        self.pay = pay
        self.company = company

    raise_amount = 1.10

    @property
    def fullname(self):
        return f'{self.firstname} {self.last}'

    def email(self):
        return f'{self.firstname}.{self.last}@{self.company}.com'

