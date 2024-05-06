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

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    raise_package_amount = 1.10

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_package_amount = amount

    @classmethod
    def emp_instance(cls, item):
        first, last, country, pack, hand, team = item.split(' ')
        return cls(first, last, country, pack, hand, team)

