class Player:
    team_run = 0       # class/static variable

    def __init__(self, run):
        self.run = run   # instance variable

    def hit_six(self):
        self.run += 6
        Player.team_run += 6

    def hit_four(self):
        self.run += 4
        Player.team_run += 4


Tamim = Player(0)
Tamim.hit_six()   # Tamim: 6, team: 6
Tamim.hit_six()   # Tamim: 12, team: 12
Tamim.hit_four()  # Tamim: 16, team: 16

Shakib = Player(2)
Shakib.hit_six()  # Shakib: 8, team: 22

print(Tamim.run)        # 16 (Tamim’s individual runs)
print(Shakib.run)       # 8  (Shakib’s individual runs)
print(Player.team_run)  # 22 (total team runs)
print(Tamim.team_run)   # 22 (accessing class var via object)
