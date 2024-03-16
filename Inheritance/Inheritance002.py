# Inheritance concepts will be covered here for better understanding.

class Bike:

    hike_amount = 1.10

    def __init__(self, brand, bike, mileage, price, displacement):
        self.brand = brand
        self.bike = bike
        self.mileage = mileage
        self.price = price
        self.displacement = displacement

    def bikeInfo(self):
        return f'Product name : {self.brand} {self.bike} {self.displacement}'

    def bikePrice(self):
        return f'Price of the bike is : {self.price}'

    @classmethod
    def set_hike_amount(cls, amount):
        cls.hike_amount = amount

    def hiked_price(self):
        self.price = self.hike_amount * self.price
        return f'product price after hiked : {self.price}'

    @classmethod
    def bikeInstance(cls, line):
        brand, bike, mileage, price, displacement = line.split(' ')
        return cls(brand, bike, mileage, price, displacement)


class Scooter(Bike):

    hike_amount = 0.75
    def __init__(self, brand, bike, mileage, price, displacement, groundClearance):
        super().__init__(brand, bike, mileage, price, displacement)
        self.groundClearance = groundClearance

    def bikeGroundClearance(self):
        return f'Ground clearance of the bike is : {self.groundClearance}'

activa5g = Scooter('Honda', 'activa', 45, 85000,
                   110, 123)

class Auto(Bike):

    hike_amount = 2.2

    def __init__(self, brand, bike, mileage, price, displacement, weight=None):
        super().__init__(brand, bike, mileage, price, displacement)
        if self.weight is None:
            self.weight = []
        else:
            self.weight = weight

    def add_vehicle(self, vehicle):
        if vehicle not in self.weight:
            self.weight.append(vehicle)
        else:
            pass

    def remove_vehicle(self, vehicle1):
        if vehicle1 in self.weight:
            self.weight.remove(vehicle1)
        else:
            pass

    def print_vehicles(self, vehicles2):
        for vehicles2 in self.weight:
            print(f'---> {vehicles2}')







print(activa5g.bikeInfo())
print(activa5g.bikePrice())
activa5g.set_hike_amount(1.10)
print(activa5g.hiked_price())

