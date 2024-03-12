# difference in class variable and instance variable.

class Apple_iphone_sale:

    gstTax = 30000  # class variable will be same for all the instances.
    total_sale = 0  # class variable only for this class.


    def __init__(self, brand, model, generation, battery, basePrice, storage):
        self.brand = brand
        self.model = model
        self.generation = generation
        self.battery = battery
        self.basePrice = basePrice
        self.storage = storage

        Apple_iphone_sale.total_sale += 1

    def fullname(self):
        print(f'the name of phone is : {self.brand} {self.model} {self.generation}')

    def rom(self):
        self.basePrice = self.basePrice + self.gstTax
        return self.basePrice




print(Apple_iphone_sale.total_sale)
print(f'---------------------------')

iphone13 = Apple_iphone_sale('Apple', 'iphone', 13,
                             4500, 60000, 256)
iphone12 = Apple_iphone_sale('Apple', 'iphone', 12,
                             4000, 40000, 128)
iphone14 = Apple_iphone_sale('Apple', 'iphone', 14,
                             4400, 70000, 256)

print(iphone13.rom())
print(iphone12.rom())
print(iphone14.rom())


print(f'the total number of sales of the devices : {Apple_iphone_sale.total_sale}')






