class Employee:

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    raise_amount = 1.10

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def emp_instance(cls, item):
        first, last, pay, company = item.split(' ')
        return cls(first, last, pay, company)

    def apply_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_amount))

