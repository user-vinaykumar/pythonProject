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

    @classmethod
    def emp_instance(cls, item):
        first, last, pay, comp = item.split('-')
        return cls(first, last, pay, comp)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def fullname(self):
        return f'full name of the employee is : {self.firstname} {self.lastname}'

    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.company}.com'

    def __repr__(self):
        return f'name of the employee : {self.firstname} {self.lastname}'

    def __str__(self):
        return f'email of the employee : {self.email()}'

    def __add__(self, other):
        return self.pay + other.pay


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

    def print_emp(self):
        for emp in self.employees:
            print(f'--> {emp.fullname()}, {emp.email()}')

emp1 = Employee('sharan', 'gs', 500, 'aplha')
emp2 = Employee('swaroop', 'nu', 500, 'alpha')
cls1 = 'vinay-kumar-80000-virtusa'
cls2 = Employee.emp_instance(cls1)
print(cls2.pay)
print(emp1 + emp2)
manager1 = Manager('srinivas', 'muddduluru',
                   60000, 'virtusa', [emp2, emp1])

manager1.print_emp()

