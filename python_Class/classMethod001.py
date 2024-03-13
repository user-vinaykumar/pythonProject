# setting up the class variables assignment by assigning the class variables with
# values using class methods.

class Mobilephones:

    tax = 1.50
    phonesale = 0

    def __init__(self, brand, model, generation, price):
        self.brand = brand
        self.model = model
        self.generation = generation
        self.price = price

        Mobilephones.phonesale += 1

    def fullName(self):
        return (f'full name of the mobile phone is : {self.brand} '
                f'{self.model} {self.generation}')

    def totalcost(self):
        self.price = int(self.price * self.tax)
        return self.price

    @classmethod
    def setTaxrate(cls, taxrate):  # assinging class variable with value using class method.
        cls.tax = taxrate           # so that the dynamic coding will be achieved.

    @classmethod
    def from_string(cls, phone_string): # alternative constructor where we are telling this class to take the string input
        brand, model, generation, price = phone_string.split('-') # as separate variable assignment.
        return cls(brand, model, generation, price)

iphone13 = Mobilephones('Apple', 'iphone', 13, 60000)
print(iphone13.totalcost())
Mobilephones.setTaxrate(2.0)
print(iphone13.totalcost())

my_phone1 = 'samsung-galaxy-s23-70000'
my_phone2 = 'motorola-g44-4-23000'

print(Mobilephones.phonesale)
print(f'--------------')
newphone1 = Mobilephones.from_string(my_phone1)
newphone2 = Mobilephones.from_string(my_phone2)
print(Mobilephones.phonesale)

print(newphone1.fullName())
print(newphone2.fullName())

print(Mobilephones.phonesale)




