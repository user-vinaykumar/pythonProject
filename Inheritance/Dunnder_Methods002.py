# dunnder methods part 2

class Employee:

    raise_amount = 1.10

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    def fullname(self):
        return f'full name : {self.firstname} {self.lastname}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.amount = amount

    def __add__(self, other):
        return self.pay + other.pay

    def __str__(self):
        return (f'name : {self.firstname}\n '
                f'company : {self.company}\n '
                f'pay : {self.pay}')


class Developer(Employee):

    def __init__(self, firstname, lastname, pay, company, proglang):
        super().__init__(firstname, lastname, pay, company)
        self.proglang = proglang


    def programming(self):
        return f'language he is performing : {self.proglang}'

    # def __len__(self):
    #     return f'length of the fullname of the employee is {len(self.fullname())}'


class Manager(Employee):

    def __init__(self, firstname, lastname, pay, company, employees=None):
        super().__init__(firstname, lastname, pay, company)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            pass

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            pass

    def print_emp(self):
        for emp in self.employees:
            print(f'--> {emp.fullname()}')


emp1 = Employee('vinay', 'kumar', 60000, 'Virtusa')
emp2 = Employee('spoorthi', 'nu', 80000, 'Cognizant')

dev1 = Developer('vinay', 'gs', 30000, 'Virtusa',
                 'Python')
dev2 = Developer('spoorthi', 'nu', 70000, 'Cognizant',
                 'Java')
print(dev1 + emp2)
print(dev2)
manager1 = Manager('srinivas', 'mudduluru', 90000,
                   'Virtusa', [dev2, dev1])
print(f'---------------')
print(manager1)








