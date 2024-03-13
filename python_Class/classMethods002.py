# class methods practice.

class Laptops:

    govt_tax = 0
    def __init__(self, brand, model, graphics, price, ram):
        self.brand = brand
        self.model = model
        self.graphics = graphics
        self.price = price
        self.ram = ram

    def laptopName(self):
        return f'the brand name of the laptop is {self.brand} {self.model}'

    @classmethod
    def set_govtTax(cls, percentage):
        cls.govt_tax = percentage


    def totalcost(self):
        self.price = self.govt_tax * float(self.price)
        return int(self.price)

    @classmethod
    def classmethodInstance(cls, item):
        brand, model, graphics, price, ram = item.split('-')
        return cls(brand, model, graphics, price, ram)

exam1 = 'dell-fens-nvidia-70000-32'
exam2 = 'apple-macbook-swif-90000-64'

inst1 = Laptops.classmethodInstance(exam1)
inst2 = Laptops.classmethodInstance(exam2)

print(inst1.laptopName())
print(inst2.laptopName())
print(inst2.price)
print(inst1.price)
Laptops.set_govtTax(1.18)
print(inst1.totalcost())
print(inst2.totalcost())

