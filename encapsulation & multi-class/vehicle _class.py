# alternate way of creating object using @classmethod
class Car:
    tier_inch = 15
    
    def __init__(self, name, cc):
        self.name = name
        self.cc = cc

    def car_info(self):
        print(f"Car Name: {self.name}")
        print(f"Engine Capacity: {self.cc}")
        print(f"Wheel in inch: {Car.tier_inch}")

    @classmethod
    def update_tier(cls, inch):
        cls.tier_inch = inch

    @classmethod
    def from_string(cls, car_data):   
        name, cc = car_data.split("_")
        return cls(name, int(cc))     # cast cc to int


car1 = Car("Mercedes", 3000)
car2 = Car.from_string("Morris Garage_2000")  # alternative constructor

car1.car_info()
car2.car_info()
