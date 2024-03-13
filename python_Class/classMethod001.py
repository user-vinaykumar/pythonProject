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

iphone13 = Mobilephones('Apple', 'iphone', 13, 60000)
print(iphone13.totalcost())
Mobilephones.setTaxrate(2.0)
print(iphone13.totalcost())


