# Concepts of Dunnder methods.

class Employee:
    raise_amount = 1.10
    def __init__(self, firstname, lastname, pay, company):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.company = company

    def fullname(self):
        return f'full name : {self.firstname} {self.lastname}'

    def email(self):
        return f'email : {self.firstname}.{self.lastname}@{self.company}.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f'{self.firstname} {self.lastname} {self.pay} {self.company}'

    def __str__(self):
        return f'{self.fullname()} {self.email()}'

emp1 = Employee('vinay', 'kumar', 60000, 'Virtusa')
print(emp1) # returns the dunnder method (__repr__) whenever we print the emp object.
            # we can define the dunnder method as we defined here now.
print(f'-----------')
print(emp1)

# if we do not use __str__ dunnder the __repr__ will have more importance
# if we use __str__ then, we have __repr__ is of no use since the object will first see the str dunnder.
