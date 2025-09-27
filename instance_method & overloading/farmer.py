class Farmer:
    def __init__(self, a = None):
        self.crops_list = []
        self.fishes = []
        if a == None:
            print(f"Welcome to your farm!")
        elif type(a) == str:
            print(f"Welcome to your farm, {a}!")
        elif type(a) == int:
            print(f"Welcmoe to your farm. Your Id is {a}")


    def addCrops(self, *crops):
        if len(crops) == 0:
            print(f"No crops added")
        else:
            print(f"{len(crops)} crops added")
            for i in crops:
                self.crops_list.append(i)

    def addFishes(self, *fish):
        if len(fish) == 0:
            print(f"No fishes added")
        else:
            print(f"{len(fish)} were added")
            for i in fish:
                self.fishes.append(i)
    def showGoods(self):
        if len(self.crops_list) == 0:
            print(f"You don't have any crops")
        else:
            print(f"You have {len(self.crops_list)} crops:")
            for i in self.crops_list:
                print(i, end = ",")
            print()


        if len(self.fishes) == 0:
            print(f"You don't have any fish")
        else:
            print(f"You have {len(self.fishes)} fish:")
            for i in self.fishes:
                print(i, end = ",")
            print()

f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")
