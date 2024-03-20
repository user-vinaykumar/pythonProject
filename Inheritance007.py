# Inheritance concepts by corey schafer.

class Employee:

    raise_amount = 1.10

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    def fullname(self):
        return f'full name is : {self.firstname} {self.lastname}'

    def email(self):
        return f'mail ID : {self.firstname}.{self.lastname}@{self.company}.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

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
            print(f'--> {emp.fullname()}')

class JuniorDeveloper(Developer):

    def __init__(self, firstname, lastname, pay, company, rms=None):
        super().__init__(firstname, lastname, pay, company)
        if rms is None:
            self.rms = []
        else:
            self.rms = rms

    def rmsdetails(self):
        if self.rms is []:
            return 'the list is empty'
        else:
            return self.rms

dev1 = Developer('spoorthi', 'nu', 60000, 'Cognizanr',
                 'Java')
dev2 = Developer('vinay', 'kumar', 70000, 'Virtusa',
                 'Python')
dev3 = Developer('sharan', 'GS', 50000, 'Accenture',
                 'Javascript')
manager1 = Manager('Srinivas', 'Muddulur', 90000, 'Virtusa',
                   [dev2, dev1])

print(manager1.company)
manager1.print_emp()
print(f'-----------------')
manager1.add_emp(dev3)
manager1.print_emp()
print(f'----------------')
print(dev2.email())
print(dev1.email())
print(dev3.email())
print(f'--------------------')
print(dev3.raise_amount)
print(dev2.raise_amount)
print(dev1.raise_amount)
print(f'------------------')
manager1.remove_emp(dev3)
manager1.print_emp()


