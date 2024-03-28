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

    @property
    def email(self):
        return f'{self.firstname}.{self.last}@{self.company}.com'

    @fullname.setter
    def fullname(self, name):
        first, lastname = name.split(' ')
        self.firstname = first
        self.last = lastname

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def emp_instance(cls, item):
        firs, las, pa, com = item.split(' ')
        return cls(firs, las, pa, com)

    def apply_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_amount))

