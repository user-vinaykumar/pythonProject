# topics of Inheritance being practised.

class Employee:

    raise_amount = 1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullName(self):
        return f'{self.first} {self.last}'

    def email(self):
        return f'{self.first}{self.last}@company.com'

    def set_raise_amount(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

class Developer(Employee):
    def __init__(self, first, last,pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    raise_amount = 1.10

dev2 = Developer('arun', 'kumar', 50000, 'Java')
emp1 = Employee('sharan', 'gs', 60000)

dev1 = Developer('vinay', 'kumar', 70000, 'Python')
print(dev1.raise_amount)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(dev2.raise_amount)



