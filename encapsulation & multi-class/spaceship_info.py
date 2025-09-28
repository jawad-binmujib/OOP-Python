class Cargo:
    def __init__(self, item_name, item_weight):
        self.__item_name = item_name
        self.__item_weight = item_weight
    def getName(self):
        return self.__item_name
    def getWeight(self):
        return self.__item_weight
class Spaceship:
    def __init__(self, spaceship_name , spaceship_cc):
        self.spaceship_name  = spaceship_name
        self.spaceship_cc = spaceship_cc
        self.cargo_list =  []
        self.total_weight = 0

    def load_cargo(self, cargo_item_name):
        self.cargo_item_name = cargo_item_name

        cargo_item_weight = cargo_item_name.getWeight()
        cargo_item_name = cargo_item_name.getName()
        self.total_weight += cargo_item_weight
        if self.total_weight < self.spaceship_cc:
            self.cargo_list.append(cargo_item_name)
        else:
            print(f"Unable to load {cargo_item_name} inside {self.spaceship_name}. Exceeds capacity by {self.total_weight-self.spaceship_cc}")
            self.total_weight -= cargo_item_weight

    def display_details(self):
        print(f"Spaceship Name:{self.spaceship_name}")
        print(f"Capacity: {self.spaceship_cc}")
        print(f"Current Cargo Weight:{self.total_weight}")
        print(f"Cargo:{self.cargo_list}")




falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold) # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium) # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium) # This should not exceed Enterprise's capacity
enterprise.display_details()