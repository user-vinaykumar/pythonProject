class Employee:

    raise_amount = 1.10
    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.company}.com'

    def apply_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_amount))

    @classmethod
    def emp_instance(cls, item):
        first, last, pay, comp = item.split(' ')
        return cls(first, last, pay, comp)

