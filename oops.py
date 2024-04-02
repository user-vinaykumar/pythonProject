class Employee:

    raise_amount = 1.10
    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.company}.com'

    def apply_raise(self):
        self.pay = int(float(self.pay) * float(self.raise_amount))

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def emp_instance(cls, item):
        first, last, pay, comp = item.split(' ')
        return cls(first, last, pay, comp)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    def __repr__(self):
        return f'{self.fullname}'

    def __str__(self):
        return f'{self.email}'

    def __add__(self, other):
        return self.pay + other.pay

class Developer:

    def __init__(self, firstname, lastname, pay, company, prog_lang):
        super().__init__(firstname, lastname, pay, company)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, firstname, lastname, pay, company, employeeslist=None):
        super().__init__(firstname, lastname, pay, company)
        if employeeslist is None:
            self.employeelist = []
        else:
            self.employeelist = employeeslist

    def add_emp(self, emp):
        if emp not in self.employeelist:
            self.employeelist.append(emp)
        else:
            pass

    def remove_emp(self, emp):
        if emp in self.employeelist:
            self.employeelist.remove(emp)
        else:
            pass

    def print_emp(self):
        for emp in self.employeelist:
            print(f'--> {emp.fullname}')




emp1 = Employee('vinay', 'kumar', 900, 'virtusa')
dev1 = Developer('spoorthi', 'nu', 800, 'cognizant',
                 'java')

print(dev1.prog_lang)