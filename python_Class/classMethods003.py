# class methods for assigning variables.

class Railways:

    def __init__(self, name, time, source, destination):
        self.name = name
        self.time = time
        self.source = source
        self.destination = destination

    def trainName(self):
        return f'train name is {self.name}'
    def trainNameDestination(self):
        return f'train name is {self.name} and destination is {self.destination}'


    @classmethod
    def railInfo(cls, item):
        name, time, source, destination = item.split('-')
        return cls(name, time, source, destination)


example1 = 'tippu express-10:30am-bengaluru-mysuru'
example2 = 'chennamma express-11:45pm-bengaluru-hubballi'
inst2 = Railways.railInfo(example2)
inst1 = Railways.railInfo(example1)

print(inst1.time)
print(inst2.name)

print(inst2.trainNameDestination())
