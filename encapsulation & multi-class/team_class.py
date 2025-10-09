class Team:
  def __init__(self, team_name=''):
    self.__team_name = team_name
    self.__player = []
  def setName(self, team_name):
    self.__team_name = team_name
  def addPlayer(self, player):
    self.__player.append(player.name)
  def printDetail(self):
    print(f"=====================")
    print(f"Team:{self.__team_name}")
    print(f"List of Players:")
    print(f"{self.__player}")
    print(f"=====================")
class Player:
  def __init__(self, name):
    self.name = name
b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()