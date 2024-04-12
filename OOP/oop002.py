class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    raise_percent = 1.10

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.company}.com'


