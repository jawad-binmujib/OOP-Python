class Hotel():

    def __init__(self, category, price):
        self.room_types = category
        self.cost = price


    def package(self):
        print("Room:",self.room_types,"\nExpense:",self.cost)

guest1 = Hotel("president", 25000)
guest2 = Hotel("deluxe", 15000)
guest3 = Hotel("Single", 10000)
guest1.package()
guest2.cost = 12000
guest2.package()
guest3.package()