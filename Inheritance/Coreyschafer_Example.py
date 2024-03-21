# Inheritance concept covering.

class Employee:
    raise_amount = 1.10
    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.last = lastname
        self.pay = pay
        self.company = company

    def fullname(self):
        return f'full name : {self.firstname} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def email(self):
        return f'email : {self.firstname}.{self.last}@{self.company}.com'

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

class Developer(Employee):
    def __init__(self, firstdev, lastdev, paydev, devcompany, prog_lang):
        super().__init__(firstdev, lastdev, paydev, devcompany)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, firstman, lastman, payman, mancompany, employees=None):
        super().__init__(firstman, lastman, payman, mancompany)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp in self.employees:
            pass
        else:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            pass

    def print_emp(self):
        for emp in self.employees:
            print(f'--> {emp.fullname()}')

dev1 = Developer('vinay', 'kumar', 50000, 'Virtusa',
                 'Python')
dev2 = Developer('spoorthi', 'nu', 60000, 'Cognizant',
                 'Java')
dev3 = Developer('Sharan', 'gs', 70000, 'Accenture',
                 'Javascript')
manager1 = Manager('Swaroop', 'nu', 80000, 'Infosys',
                   [])

print(dev1.pay)
print(dev1.raise_amount)
dev1.apply_raise()
print(dev1.pay)
print(f'----------------')
print(dev2.raise_amount)
dev2.set_raise_amount(1.20)
dev2.apply_raise()
print(dev2.pay)
print(dev2.raise_amount)
print(dev3.email())
print(f'-----------------')
manager1.print_emp()
manager1.add_emp(dev2)
manager1.print_emp()
manager1.add_emp(dev1)
manager1.print_emp()



