

class Grandfather:
    def __init__(self, name, dob, loc):
        # Initialize Grandfather attributes
        self.name = name
        self.dob = dob
        self.loc = loc

    def metA(self):
        print("metA of Grandfather class has been created")

class Parent(Grandfather):
    def __init__(self, name, dob, loc):
        # Call Grandfather's constructor to initialize attributes
        super().__init__(name, dob, loc)

    def metB(self):
        print("metB of Parent class has been created")

class Child(Parent):
    def __init__(self, name, dob, loc):
        # Call Parent's constructor to initialize attributes
        super().__init__(name, dob, loc)

    def metC(self):
        print("metC of Child class has been created")

# Create an instance of Child and demonstrate inherited methods
c2 = Child("jawad", 12345, "ctg")
c2.metA()  # method of Grandfather
c2.metB()  # method of Parent
c2.metC()  # method of Child