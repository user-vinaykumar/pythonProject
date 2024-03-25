# corey schafer python oops.

class Employee:

    raise_amount = 1.10

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    @property
    def fullname(self):
        return f'full name : {self.firstname} {self.lastname}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    @property
    def email(self):
        return (f'email of the employee is : {self.firstname}{self.lastname}'
                f'@{self.company}.com')

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def emp_instance(cls, item):
        first, last, pay, company = item.split(' ')
        return cls(first, last, pay, company)

    def __repr__(self):
        return f'{self.fullname}'

    def __str__(self):
        return f'{self.email}'

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
            print(f'--> {emp.fullname}')

emp1 = Employee('vinay', 'kumar', 500, 'abc')
emp2 = Employee('spoorthi', 'nu', 600, 'efg')
dev1 = Developer('sharan', 'gs', 700, 'xyz'
                 , 'C#')
dev2 = Developer('swaroop', 'nu', 600, 'jkl',
                 'Javascript')

manager1 = Manager('srinivas', 'muddulur', 900,
                   'abc', [emp2, emp1, dev1])


manager1.print_emp()
manager1.remove_emp(dev1)
print(f'-------------')
manager1.print_emp()
manager1.add_emp(dev2)
print(f'-----------')
manager1.print_emp()
manager1.add_emp(dev1)
print(f'-------------')
manager1.print_emp()

print(dev1.fullname)
print(emp1.fullname)
print(emp2.fullname)
print(dev2.fullname)
print(dev1.email)
dev1.fullname = 'sharan gudigenahalli'
print(dev1.email)
dev1.raise_amount = 1.20
print(dev1.raise_amount)
print(emp1.raise_amount)
