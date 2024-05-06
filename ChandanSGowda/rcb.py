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

    def apply_raise(self):
        self.package = int(float(self.package) * float(self.raise_package_amount))

    def __repr__(self):
        return self.fullname

    def __str__(self):
        return self.package

    def __add__(self, other):
        return self.package + other.package

class Batsman(Players):

    def __init__(self, firstname, lastname, country, package, handed, team, language):
        super().__init__(firstname, lastname, country, package, handed, team)
        self.language = language

class Coach(Players):

    def __init__(self, firstname, lastname, country, package, handed, team, playerlist=None):
        super().__init__(firstname, lastname, country, package, handed, team)
        if playerlist is None:
            self.playerlist = []
        else:
            self.playerlist = playerlist

    def add_players(self, member):
        if member not in self.playerlist:
            self.playerlist.append(member)
        else:
            pass

    def remove_players(self, member):
        if member in self.playerlist:
            self.playerlist.remove(member)
        else:
            pass


    def print_players(self):
        for players in self.playerlist:
            print(f'--> {players.fullname}')


