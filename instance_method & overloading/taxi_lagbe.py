class TaxiLagbe:
    def __init__(self, taxi_no, area):
        self.taxi_no = taxi_no
        self.area = area
        self.passenger = []
        self.total_fare = 0
        self.capacity = 4

    def addPassenger(self, *args):
        if len(self.passenger) >= self.capacity:
            print("Taxi Full! No more passengers can be added.")
            return

        for passenger in args:
            name, fare = passenger.split('_')
            self.passenger.append(name)
            self.total_fare += int(fare)
            print(f"Dear {name}! Welcome to TaxiLagbe.")

    def printDetails(self):
        print(f"Trip info for Taxi number: {self.taxi_no}")
        print(f"This taxi can only cover the {self.area} area.")
        print(f"Total passengers: {len(self.passenger)}")
        print("Passenger lists:")
        print(", ".join(self.passenger))
        print(f"Total collected fare: {self.total_fare} Taka")

# Driver Code
taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200','Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115', 'Parker_215')
print('-------------------------------')
taxi2.printDetails()