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

    def __repr__(self):
        return f'{self.email}'

    def __str__(self):
        return f'{self.fullname}'

    def __add__(self, other):
        return self.pay + other.pay

class Developer(Employee):

    def __init__(self, firstname, las, pay, comp, prog):
        super().__init__(firstname, las, pay, comp)
        self.prog = prog

