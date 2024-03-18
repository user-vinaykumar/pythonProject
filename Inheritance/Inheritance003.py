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

class Manager(Employee):

    raise_amount = 1.20

    def __init__(self, firstName, lastName, pay, emps=None):
        super().__init__(firstName, lastName, pay)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps

    def add_emp(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)
        return self.emps

    def remove_emp(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)
        return self.emps

    def print_emps(self):
        for emp in self.emps:
            print(f'--> {emp.fullName()}')

class JuniorDeveloper(Developer):

    def __init__(self, firstName, lastName, pay, prog_lang, noye):
        super().__init__(firstName, lastName, pay, prog_lang)
        self.noye = noye

    def numberOfExperience(self):
        return f'Junior Developer has {self.noye} years of experience'

dev2 = Developer('spoorthi', 'nu', 60000, 'Java')
dev1 = Developer('vinay', 'kumar', 75000, 'Python')

manager1 = Manager('srinivas', 'muddulur', 70000, [])

jd1 = JuniorDeveloper('sharan', 'gs', 40000,
                      'JavaScript', 2)



manager1.add_emp(dev2)
manager1.add_emp(dev1)
manager1.remove_emp(dev2)

print(manager1.print_emps())
print(jd1.numberOfExperience())
print(jd1.fullName())
manager1.add_emp(jd1)
print(manager1.print_emps())



