# create class with self instance.

class Railways():
    def __init__(self, name, ID, phone, location, train):
        self.name = name
        self.ID = ID
        self.phone = phone
        self.location = location
        self.train = train


rail1 = Railways('vinay', 8114006, 7899097827, 'Bengaluru',
                 'Tippu Express')

print(rail1.name)
print(rail1.location)
print(rail1.train)
print('------------------')
rail2 = Railways('sharan', 8334665, 73385278, 'Mysuru',
                 'Chennamma Express')

print(rail2.name)
print(rail2.location)
print(rail2.train)

