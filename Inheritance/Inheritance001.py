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

    def raise_salary(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

class Developer(Employee):
    def __init__(self, first, last,pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    raise_amount = 1.10

emp1 = Employee('sharan', 'gs', 60000)
emp2 = Employee('swaroop', 'nu', 90000)

dev1 = Developer('vinay', 'kumar', 70000, 'Python')
dev2 = Developer('spoorthi', 'nu', 80000, 'Java')
print(dev1.raise_amount)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(dev2.raise_amount)

print(emp2.raise_salary())
print(dev2.raise_salary())
print(dev1.fullName())
print(dev2.fullName())
print(emp2.fullName())
print(emp1.fullName())
print(emp1.email())
print(emp2.email())
print(dev2.email())
print(dev1.email())

class Manager(Employee):

    def __init__(self, first, last, pay, emp_list=None):
        super().__init__(first, last, pay)
        if emp_list is None:
            self.emp_list = []
        else:
            self.emp_list = emp_list

    def add_emp(self, emp):
        if emp not in self.emp_list:
            return self.emp_list.append(emp)


    def remove_emp(self, emp):
        if emp in self.emp_list:
            return self.emp_list.remove(emp)

    def emps_under_manager(self):
        for emp in self.emp_list:
            return f'--> {emp.fullName()}'

manager1 = Manager('srinivas', 'muddulur', 80000, [dev2])
print(manager1.emps_under_manager())
print(manager1.add_emp(dev2))




