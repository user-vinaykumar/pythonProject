class Players():

    def __init__(self, firstname, lastname, country, package, handed, team):
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.package = package
        self.handed = handed
        self.team = team


    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.team}.com'

