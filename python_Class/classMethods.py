# class methods takes cls (class as argument) but regular methods take self as arguments.

class Employee:

    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay

        Employee.num_of_emp += 1


    def fullName(self):
        return f'The full name of an Employee is : {self.firstName} {self.lastName}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amount = amount
        return cls.raise_amount



emp1 = Employee('vinay', 'kumar', 50000)
emp2 = Employee('sharan', 'gs', 60000)

emp2.set_raise(1.05)
print(emp2.apply_raise())

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
