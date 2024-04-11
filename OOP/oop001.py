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

    def apply_percentage_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_percent))

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.company}.com'

