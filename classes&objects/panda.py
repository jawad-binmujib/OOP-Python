class Panda:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def sleep(self, hours):
        if 3<= hours <= 5:
            return (f"{self.name} sleeps {hours} hours daily and should have Mixxed Veggies")
        elif 6<= hours <= 8:
            return (f"{self.name} sleeps {hours} hours daily and should have Eggplant & Tofu")
        elif 9<= hours <= 11:
            return (f"{self.name} sleeps {hours} hours daily and should have Broccoli Chicken")
        else:
            return (f"{self.name} sleeps {hours} hours daily and should have bamboo leaves")
panda1 = Panda("Kunfu", "Male", 5)
panda2 = Panda("Pan Pan", "Female",3)
panda3 = Panda("Ming Ming", "Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep(13))