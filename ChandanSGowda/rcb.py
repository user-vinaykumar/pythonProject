class RoyalChallengersBengaluru():

    def __init__(self, firstname, lastname, country, package, handed):
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.package = package
        self.handed = handed


    def fullname(self):
        return f'{self.firstname} {self.lastname}'

