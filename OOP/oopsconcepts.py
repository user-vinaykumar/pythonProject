class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.compnay = company

    raise_percent = 1.10

    def fullname(self):
        return f'{self.firstname} {self.lastname}'
