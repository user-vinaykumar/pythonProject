# inheritance concepts understanding.

class Home:

    site_dimensions = '30-40'
    def __init__(self, livingroom, kitchen, bathroom, deityroom, bedroom):
        self.livingroom = livingroom
        self.kitchen = kitchen
        self.bathroom = bathroom
        self.deityroom = deityroom
        self.bedroom = bedroom


    @classmethod
    def set_site_dimensions(cls, dimensionitem):
        cls.site_dimensions = dimensionitem


    def showKitchen(self):
        return f'Kitchen would be : {self.kitchen}'

    def showBathroom(self):
        return f'Bathroom would be : {self.bathroom}'

    def showLivingroom(self):
        return f'Livingroom would be : {self.livingroom}'

    def showBedroom(self):
        return f'Bedroom would be : {self.bedroom}'

    def showDietyroom(self):
        return f'Dietyroom would be : {self.deityroom}'

