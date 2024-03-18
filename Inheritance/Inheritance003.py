# inheritance concepts practised here.

class Employee:
    raise_amount = 1.05
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay

    def fullName(self):
        return f'full name of the employee is : {self.firstName} {self.lastName}'

    def raised_salary(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    def email(self):
        return f'email of the employee is : {self.firstName}{self.lastName}@company.com'


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, firstName, lastName, pay, prog_lang):
        super().__init__(firstName, lastName, pay)
        self.prog_lang = prog_lang

    def programmingLang(self):
        return f'language the developer is using {self.prog_lang}'

