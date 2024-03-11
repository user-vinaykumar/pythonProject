class Team:
    def __init__(self, name, captain, win, ban):
        self.name = name
        self.captain = captain
        self.win = win
        self.ban = ban

rcb = Team('Royal Challengers Bengaluru', 'Virat Kohli',
           0, 0)
csk = Team('Chennai Super Kings', 'Mahendra Singh Dhoni',
           4, 2)

print(rcb.name)
print('---------')
print(csk.name)