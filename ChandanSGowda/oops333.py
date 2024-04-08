class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    raise_amount = 1.10

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

