class Tournament:
    def __init__(self, name='Default'):
        # Private attribute for tournament name
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class CricketTournament(Tournament):
    def __init__(self, name='Default', team=0, type="No type"):
        super().__init__(name)
        self.team = team    # Number of teams
        self.type = type    # Tournament type

    def detail(self):
        return (
            f"Cricket Tournament Name: {self.get_name()} \n"
            f"Number of Teams: {self.team}\n"
            f"Type : {self.type}"
        )

class TennisTournament(Tournament):
    def __init__(self, name, numb):
        super().__init__(name)
        self.numb = numb    # Number of players

    def detail(self):
        return (
            f"Tennis Tournament Name : {self.get_name()} \n"
            f"Number of Players : {self.numb}"
        )

# Demonstrate usage
ct1 = CricketTournament()
print(ct1.detail())
print("-----------------------")
ct2 = CricketTournament("IPL", 10, "t20")
print(ct2.detail())
print("-----------------------")
tt = TennisTournament("Roland Garros", 128)
print(tt.detail())