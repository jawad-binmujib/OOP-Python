class Player:
  total = 0
  players_list = []
  def __init__(self, player_name = None, player_number=10, team=None):
    self.player_name = player_name
    self.player_number = player_number
    self.team = team
    if player_name:
      Player.total += 1
      Player.players_list.append(player_name)
  def set_name(self, player_name):
    self.player_name = player_name
    Player.total += 1
    Player.players_list.append(player_name)
  def set_number(self, player_number):
    self.player_number = player_number
  def set_team(self, team):
    self.team = team
  def player_detail(self):
    return f"Player player name: {self.player_name}\nJersey player number: {self.player_number}\nCountry: {self.team}"
  @classmethod
  def info(cls):
    print(f"Total number of players : {cls.total}")
    print(f"Players enlisted so far: {', '.join(Player.players_list)}")


print("Total number of players:", Player.total)
print("---------------------------")
p1 = Player()
p1.set_name("Neymar")
p1.set_team("Brazil")
print(p1.player_detail())
print('========================')
Player.info()
print("---------------------------")
p2 = Player("Ronaldo")
p2.set_number(7)
p2.set_team("Portugal")
print(p2.player_detail())
print('========================')
Player.info()
print("---------------------------")
p3 = Player("Messi")
p3.set_team("Argentina")
print(p3.player_detail())
print('========================')
Player.info()
print("---------------------------")
p4 = Player("Mbappe", 10, "France")
print(p4.player_detail())
print('========================')
Player.info()
