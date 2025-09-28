class Car:
    wheel_size = 16

    def __init__(self, car_name, car_cc):
        self.car_name = car_name
        self.car_cc = car_cc

    def info(self):
        print(f"Car Name: {self.car_name}")
        print(f"Car cc: {self.car_cc}")
        print(f"Wheel: {Car.wheel_size}")

    @classmethod
    def update_wheel(cls, inch):
        cls.wheel_size = inch

    @classmethod
    def from_string(cls, data):   
        car_name, car_cc = data.split("@")
        return cls(car_name, int(car_cc))  # convert cc to int


car1 = Car("BMW", 3000)
car2 = Car("Audi", 2000)

car1.info()
print("-------------------------------------------------------")
Car.update_wheel(18)
car2.info()
car1.info()
print("-------------------------------------------------------")
car3 = Car.from_string("Mercedes@1800")
car3.info()
