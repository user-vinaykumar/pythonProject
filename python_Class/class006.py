# create a class and instances of it.

class Mobilephones:

    def __init__(self, brand, model, generation, price, rankings):
        self.brand = brand
        self.model = model
        self.generation = generation
        self.price = price
        self.rankings = rankings

    def fullname(self):
        return f'the full name of the mobile phone is : {self.brand}{self.model}'

vinay = Mobilephones('Apple', 'iphone', 13, 60000, 1)
sharan = Mobilephones('Samsung', 'Galaxy', 'S23', 15000, 21)

print(vinay.rankings)
print(vinay.model)
print(f'--------------------')
print(sharan.model)
print(sharan.price)
print(f'----------------')
print(vinay.fullname())
print(sharan.fullname())


