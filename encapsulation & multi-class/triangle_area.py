class Triangle:
    def __init__(self, base, height):
        self.__height = height
        self.__base = base
    def getBase(self):
        return self.__base
    def getHeight(self):
        return self.__height
    def setBase(self):
        pass
    def setHeight(self):
        pass
    def area(self):
        self.area = 0.5*self.__base*self.__height
        return self.area


t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())

t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())

