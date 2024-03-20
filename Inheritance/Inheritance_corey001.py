# Inheritance by corey schafer. Implementing his concepts here.

class Employee:

    raise_amount = 1.04

    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company
        self.email = f'{firstname}.{lastname}@{company}.com'

    def fullName(self):
        return f'full name : --> {self.firstname} {self.lastname}'

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):

    raise_amount = 1.05

    def __init__(self, firstname, lastname, pay, company, prog_lang):
        super().__init__(firstname, lastname, pay, company)
        self.prog_lang = prog_lang
#
# class Manager(Employee):
#
#     def __init__(self, firstman, lastman, manpay, mancomp, employees=None):
#         super().__init__(firstman, lastman, manpay, mancomp)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#         else:
#             pass
#
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#         else:
#             pass
#
#     def print_emp(self):
#         for emp in self.employees:
#             print(f'--> {emp.fullName()}')
#
#
#
# dev1 = Developer('vinay', 'kumar', 50000, 'Virtusa',
#                  'Python')
#
# dev2 = Developer('Spoorthi', 'NU', 60000,
#                  'Cognizant', 'Java')
# manger1 = Manager('Srinivas', 'Muddulur', 50000,
#                   'Virtusa', [dev2])
#
#
#
# print(dev1.pay)
# dev1.applyRaise()
# print(dev1.pay)
# print(manger1.fullName())
# print(manger1.firstname)
# print(manger1.pay)
# print(dev1.pay)
#
# manger1.add_emp(dev1)
# manger1.print_emp()
# manger1.remove_emp(dev1)
# manger1.print_emp()