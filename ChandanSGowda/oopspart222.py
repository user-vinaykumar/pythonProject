class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    raise_percent = 1.10

    @classmethod
    def set_raise_percent(cls, percent):
        cls.raise_percent = percent

    @classmethod
    def emp_instance(cls, item):
        first, last, pay, company = item.split(' ')
        return cls(first, last, pay, company)

    def apply_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_percent))

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.company}.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    def __repr__(self):
        return self.fullname

    def __str__(self):
        return self.email