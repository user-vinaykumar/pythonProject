# creating the class with self instance and performing basic operations.

class Householder:
    def __init__(self, name, area, cross, city, house):
        self.name = name
        self.area = area
        self.cross = cross
        self.house = house
        self.city = city

    def householderInfo(self):
        return (f'the house holder info is here :\n {self.name} \n'
                f'{self.area}\n {self.cross} \n {self.house} \n {self.city}')


houseHolder1 = Householder('Anasuya', 'Marigowda Layout', 1,
                           'Mandya', '#KL176')

print(houseHolder1.house)
print(houseHolder1.cross)
print(houseHolder1.householderInfo())

houseHolder2 = Householder('Jayaprakasha B', 'Rukmini Layout', 1,
                           'Ramanagara', '#123')

print(f'--------------------------')

print(houseHolder2.city)
print(houseHolder2.area)
print(houseHolder2.householderInfo())
