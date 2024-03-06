# creating a class with methods inside it.

class Employee:
    def __init__(self, first, last, email, phone, location):
        self.first = first
        self.last = last
        self.email = email
        self.mobile = phone
        self.location = location

    def fullName(self):
        print(f'the full name of the employee is : {self.first}{self.last}')




emp1 = Employee('vinay', 'kumar', 'vinay.kumar@company.com',
                78990, 'Mandya')

# print(f'full name of the employee : {emp1.first}{emp1.last}')

print(emp1.fullName())
