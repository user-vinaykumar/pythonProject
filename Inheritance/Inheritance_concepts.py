# Inheritance concepts - applying everything I learnt till now.

class Employee:

    raise_amount = 1.10

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amount = amount

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def fullname(self):
        return f'full name of the employee is : {self.firstname} {self.lastname}'

    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.company}.com'


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


