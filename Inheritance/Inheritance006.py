# Inheritance concepts and its understanding.

class Trains:
    train_type = 'superfast express'

    def __init__(self, trainname, trainsource, traindestination):
        self.trainname = trainname
        self.trainsource = trainsource
        self.traindestination = traindestination

    def traindetails(self):
        return (f'train name --> {self.trainname}\n'
                f'train source --> {self.trainsource}\n'
                f'train destination --> {self.traindestination}')

    def trainspeed(self, item):
        if item == 'superfast':
            return 'travels at 300 kmph'
        elif item == 'passenger':
            return 'travels at 80 kmph'
        elif item == 'express':
            return 'travels at 150 kmph'
        else:
            return 'you have entered wrong train type'

    @classmethod
    def set_traintype(cls, item1):
        cls.train_type = item1

class Tippu(Trains):

    def __init__(self, name, source, destination, intermediateStops):
        super().__init__(name, source, destination)
        self.intermediateStops = intermediateStops

tippu1 = Tippu('Wodeyar Express', 'Mysuru', 'Bengaluru', 2)
print(tippu1.train_type)
tippu1.set_traintype('passenger')
print(tippu1.trainspeed(tippu1.train_type))

