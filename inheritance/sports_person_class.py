

class SportsPerson:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0

    def get_name_team(self):
        return f'Name: {self.__name}, Team Name: {self.__team}'

class Player(SportsPerson):
    def __init__(self, team_name, name, role, t_goal, t_played):
        super().__init__(team_name, name, role)
        self.t_goal = t_goal
        self.t_played = t_played
        self.ratio = 0

    def calculate_ratio(self):
        if self.t_played == 0:
            self.ratio = 0
        else:
            self.ratio = self.t_goal / self.t_played

    def print_details(self):
        print(f"{self.get_name_team()}")
        print(f"Team Role: {self.role}")
        print(f"Total Goal: {self.t_goal}, Total Played: {self.t_played}")
        print(f"Goal Ratio: {self.ratio}")
        print(f"Match Earnings: {(self.t_goal * 1000) + (self.t_played * 10)}K")

class Manager(SportsPerson):
    def __init__(self, team_name, name, role, t_win):
        super().__init__(team_name, name, role)
        self.t_win = t_win

    def print_details(self):
        print(f"{self.get_name_team()}")
        print(f"Team Role: {self.role}")
        print(f"Total Win: {self.t_win}")
        print(f"Match Earnings: {self.t_win * 1000}K")


player_one = Player('Al-Nassr', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()