# create a class of laptop and add attributes.

class Mobiles:
    def __init__(self, brand, model, RAM, price, storage, storage2, screen, fingerprint):
        self.brand = brand
        self.model = model
        self.RAM = RAM
        self.price = price
        self.storage = storage
        self.storage2 = storage2
        self.screen = screen
        self.fingerprint = fingerprint

    def screencheck(self):
        print(f'the screen of the {self.brand} {self.model} is : {self.screen}')

    def pricecheck(self):
        print(f'the price of the {self.brand} {self.model} is : {self.price}')

    def fingerprintcheck(self):
        print(f'does {self.brand} {self.model} have a fingerprint scanner in it : {self.fingerprint}')

    def storagecheck(self):
        if self.price > 15000:
            print(f'the {self.brand} {self.model} has {self.storage} GB storage.')
        else:
            print(f'the {self.brand} {self.model} has {self.storage2} GB storage.')

    def phoneInfo(self):
        print(f'{self.brand} {self.model} :--')
        self.pricecheck()
        self.storagecheck()
        self.screencheck()
        self.fingerprintcheck()



iphone13 = Mobiles('Apple', 'iphone13', 32, 57000, 128,
                256, 'Amoled', False)

samsungs23 = Mobiles('Samsung', 'GalaxyS23', 16, 14999, 0,
                  32, 'Amoled', True)

oneplus12r = Mobiles('Oneplus', 'TwelveR', 64, 65000, 256,
                  0, 'Amoled', True)

realmegt = Mobiles('Realme', 'PowerGT', 64, 21000, 256,
                 0, 'Amoled', True)

redminote15 = Mobiles('Redmi', 'Note15', 64, 29000, 256,
                      0, 'LCD', False)

iphone13.phoneInfo()
print(f'----------------------')
samsungs23.phoneInfo()
print(f'-------------------------')
realmegt.phoneInfo()
print(f'-------------------')
oneplus12r.phoneInfo()
print(f'-----------------')
redminote15.phoneInfo()


