# inheritance concepts revised.

class Employee:
    raise_amount = 1.10

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def fullname(self):
        return f'full name : {self.firstname} {self.lastname}'

    def email(self):
        return (f'email of the employee : {self.firstname}.{self.lastname}'
                f'@{self.company}.com')

class Developer(Employee):

    def __init__(self, firstname, lastname, pay, company, programming_language):
        super().__init__(firstname, lastname, pay, company)
        self.programming_language = programming_language

class Manager(Employee):

    def __init__(self, firstname, lastname, pay, company, employees = None):
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


