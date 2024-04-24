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
        first, last, pay, comp = item.split(' ')
        return cls(first, last, pay, comp)

    def fullname(self):
        return f'{self.firstname} {self.lastname}'


