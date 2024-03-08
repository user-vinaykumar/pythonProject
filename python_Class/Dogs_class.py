# create animal class and initiate with instances.

class Dogs:
    def __init__(self, breed, habitat, lifespan, price):
        self.breed = breed
        self.habitat = habitat
        self.lifespan = lifespan
        self.price = price

    def dogbreed(self):
        return self.breed

    def dogprice(self):
        return self.price

    def doglifespan(self):
        return self.lifespan

    def doghabitat(self):
        return self.habitat

    def dogInfo(self):
        doglist = []
        doglist.append(self.dogbreed())
        doglist.append(self.dogprice())
        doglist.append(self.doglifespan())
        doglist.append(self.doghabitat())
        print(f'the breed of dog is {doglist[0]}\n'
              f'the price of dog is {doglist[1]}\n'
              f'the lifespan of dog is {doglist[2]}\n'
              f'the habitat of dog is {doglist[3]}')


saintBernard = Dogs('Saint Bernard', 'Switzerland', 20,
                    30000)

germanShepherd = Dogs('German Shepherd', 'Germany', 20,
                      25000)

shitzu = Dogs('Shitzu', 'China', 15, 12000)

labroder = Dogs('Labrador', 'Canada', 20, 20000)

goldenRetriever = Dogs('Golden Retriever', 'Europe', 18,
                       18000)


goldenRetriever.dogInfo()
print(f'---------------')
germanShepherd.dogInfo()
print(f'---------------')
labroder.dogInfo()
print(f'-----------------')
shitzu.dogInfo()
print(f'-----------------')
saintBernard.dogInfo()
