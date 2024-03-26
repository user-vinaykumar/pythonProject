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
        self.pay = int(self.pay * self.raise_amount)

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
            print(f'emp name --> {emp.fullname}')

emp1 = Employee('vinay', 'kumar', 500,
                'Virtusa')
emp2 = Employee('spoorthi', 'nu', 400,
                'Cognizant')
dev1 = Developer('sharan', 'gs', 700,
                 'virtusa', 'Javascript')
dev2 = Developer('swaroop', 'nu', 800,
                 'virtusa', 'Python')
manager1 = Manager('srinivas', 'muddulur', 900,
                   'virtusa', [])

print(emp1.raise_amount)
print(emp1.pay)
emp1.set_raise_amount(1.5)
emp1.apply_raise()
print(emp1.pay)

emp1.fullname = 'vinay gs'
print(emp1.fullname)
print(emp1.email)
manager1.add_emp(dev2)
manager1.add_emp(dev1)
manager1.add_emp(emp2)
manager1.print_emp()
manager1.remove_emp(dev1)
print(f'------------')
manager1.print_emp()
