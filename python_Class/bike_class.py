# create a bike class and instances.

class Bike:
    def __init__(self, brand, model, displacement, price, mileage, dualABS,
                 tankcapacity, topspeed):
        self.brand = brand
        self.topspeed = topspeed
        self.tankcapacity = tankcapacity
        self.price = price
        self.mileage = mileage
        self.dualABS = dualABS
        self.model = model
        self.displacement = displacement

    def brandInfo(self):
        return self.brand

    def modelInfo(self):
        return self.model

    def displacementInfo(self):
        return self.displacement

    def priceinfo(self):
        return self.price

    def mileageInfo(self):
        return self.mileage

    def absInfo(self):
        if self.priceinfo() > 175000:
            return self.dualABS
        else:
            return 'No dual ABS available in this machine...!!'


    def tankcapacityInfo(self):
        return self.tankcapacity

    def topspeedInfo(self):
        return self.topspeed



    def bikeinfo(self):
        print(f'Brand = {self.brandInfo()}')
        print(f'model = {self.modelInfo()}')
        print(f'bike cc = {self.displacementInfo()}')
        print(f'price of the bike = {self.priceinfo()}')
        print(f'mileage of the bike = {self.mileageInfo()}')
        print(f'does bike has ABS = {self.absInfo()}')
        print(f'tank capacity of the bike = {self.tankcapacityInfo()}')
        print(f'top speed = {self.topspeedInfo()}')


gixxerSF250 = Bike('Suzuki', 'GixxerSF250', '250cc',
                   230000, '36kmpl', True,
                   '12L', 154)

duke200 = Bike('KTM', 'Duke200', '200cc',
               240000, '32kmpl', True, '14L', 149)

r15 = Bike('Yamaha', 'R15', '150cc',
           209000, '38kmpl', True, '15L', 158)

himalayan450 = Bike('Royal Enfield', 'Himalayan450', '450cc',
                    310000, '28kmpl', True, '14L',
                    138)
rx = Bike('Yamaha', 'RX100', '100cc', 95000,
          '32kmpl', True, '12L', 121)


gixxerSF250.bikeinfo()
print(f'----------------------')
rx.bikeinfo()
print(f'--------------')
himalayan450.bikeinfo()
print(f'----------------')
duke200.bikeinfo()
print(f'------------------')
r15.bikeinfo()
