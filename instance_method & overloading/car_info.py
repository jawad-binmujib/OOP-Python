class Car():

    def __init__(self, car_name, brand):
        self.name = car_name
        self.logo = brand

    def info(self):
        print("Name of the Car:",self.name,"\nBrand of the car:",self.logo)
        print("Thanks for your enquiry")


veh1 = Car("Fielder","Toyota")
veh2 = Car("sonata","Hyundai")
#veh1.name = "premio"
veh3 = Car("Maybach","Mercedes")
veh1.info()

veh3.info()
