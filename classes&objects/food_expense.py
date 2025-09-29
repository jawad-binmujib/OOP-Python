class Food():

    def __init__(self, name, type, price):
        self.food_name = name
        self.category = type
        self.cost = price

    def menu(self):
        print("Name of the food:",self.food_name,"\nType of the food:",self.category,"\nExpense of the food is:",self.cost,"tk")


item1 = Food("Hyderabadi Biriyani","Indian", 280)
item2 = Food("Vorta","Bengali", 150)
item3 = Food("pasta","Italian", 430)

item2.menu()