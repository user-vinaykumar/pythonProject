# creating a class with methods inside it.

class Employee:
    def __init__(self, first, last, email, phone, location):
        self.first = first
        self.last = last
        self.email = email
        self.mobile = phone
        self.location = location

    def fullName(self):
        return f'{self.first} {self.last}'
        # return '{} {}'.format(self.first, self.last)

    def employeeInfo(self):
        print(f'the employee name is : {self.first} {self.last}')
        print(f'the employee email is : {self.email}')
        print(f'the employee phone is : {self.mobile}')
        print(f'the employee location is : {self.location}')





emp1 = Employee('vinay', 'kumar', 'vinay.kumar@company.com',
                78990, 'Mandya')

# print(f'full name of the employee : {emp1.first}{emp1.last}')

print(emp1.fullName())

emp2 = Employee('sharan', 'gs', 'sharangs@company.com', 73385,
                'Mandya')

print(emp2.fullName())

emp2.employeeInfo()

