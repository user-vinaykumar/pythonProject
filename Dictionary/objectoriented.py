class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.compnay = company


    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.compnay}.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    raise_amount = 1.10

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

