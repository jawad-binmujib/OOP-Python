class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def detail(self):
        return f'({self.x} , {self.y})'  

class Vehicle2010(Vehicle):
    def __init__(self, x = 0, y = 0):
        super().__init__()  # parent initialization
        self.x = x
        self.y = y

    def moveUpperRight(self):
        self.x += 1
        self.y += 1

    def moveUpperLeft(self):
        self.x -= 1
        self.y += 1

    def moveLowerRight(self):
        self.x += 1
        self.y -= 1

    def moveLowerLeft(self):
        self.x -= 1
        self.y -= 1

    def equals(self, other):
        # Check if both vehicles are at the same position
        return self.x == other.x and self.y == other.y

# Test code
print('Part 1')
print('------')
car = Vehicle()
print(car.detail())
car.moveUp()
print(car.detail())
car.moveLeft()
print(car.detail())
car.moveDown()
print(car.detail())
car.moveRight()
print(car.detail())
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1.detail())
car1.moveLowerLeft()
print(car1.detail())
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))  