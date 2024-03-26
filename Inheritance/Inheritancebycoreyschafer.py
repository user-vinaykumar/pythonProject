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

    @property
    def fullname(self):
        return f'full name of the employee : {self.firstname} {self.lastname}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    @property
    def email(self):
        return f'{self.fullname}@{self.company}.com'

    def __repr__(self):
        return f'{self.firstname} {self.pay}'

    def __add__(self, other):
        return self.pay + other.pay

    def __str__(self):
        return f'{self.email}'

class Developer(Employee):

    def __init__(self, firstname, lastname, pay, company, prog_lang):
        super().__init__(firstname, lastname, pay, company)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, firstname, lastname, pay, company, employees=None):
        super().__init__(firstname, lastname, pay, company)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            list.append(emp)
        else:
            pass

    def remove_emp(self, emp):
        if emp in self.employees:
            list.remove(emp)
        else:
            pass

