class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base

    def get_height_base(self):
        return f"Height: {self.height}, Base: {self.base}"

class Triangle(Shape):
    def __init__(self, name='Default', height=0, base=0):
        super().__init__(name, height, base)

    def calcArea(self):
        self.area = 0.5 * self.base * self.height  

    def printDetail(self):
        return f"Shape name: {self.name}\nHeight: {self.height}, Base: {self.base}\nArea: {self.area}"

class Trapezoid(Shape):
    def __init__(self, name='Default', height=0, base=0, side=0):
        super().__init__(name, height, base)
        self.side = side

    def calcArea(self):
        self.area = 0.5 * (self.base + self.side) * self.height  

    def printDetail(self):
        return f"Shape name: {self.name}\nHeight: {self.height}, Base: {self.base}, Side_A: {self.side}\nArea: {self.area}"


tri_default = Triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = Triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = Trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())