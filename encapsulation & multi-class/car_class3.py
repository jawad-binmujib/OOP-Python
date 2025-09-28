
class Engine:
    def __init__(self, cc):
        self.capacity = cc

    def start(self):
        print(f"Engine has started!")

    def stop(self):
        print(f"Engine has stopped!")

class Car:
    def __init__(self, name, cc):
        self.name = name
        self.engine = Engine(cc)

    def run (self):
        self.engine.start()
        print(f"Car is running!")

    def not_run(self):
        self.engine.stop()
        print(f"Car is not running!")


car = Car("AUDi_R8", 2000)
car.not_run()
