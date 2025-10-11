

# Parent1 class defines basic attributes and a method
class Parent1:
    def __init__(self, name, dob, loc):
        self.name = name
        self.dob = dob
        self.loc = loc

    def metA(self):
        print("metA is a method of Parent1 class")

# Parent2 inherits from Parent1; overrides metA method
class Parent2(Parent1):
    def __init__(self, name, dob, loc):
        super().__init__(name, dob, loc)  # Calls Parent1's constructor

    def metA(self):
        print("metA is a method of Parent2 class")  # This will override Parent1's metA

# Child class inherits from both Parent2 and Parent1
class Child(Parent2, Parent1):
    def __init__(self, name, dob, loc):
        super().__init__(name, dob, loc)  # Follows Python's MRO to call Parent2's __init__

    def metC(self):
        print("metC is a method of Child class")

# Create an instance of Child
c1 = Child("jawad", 234, "gulshan")

# Calls metA; due to MRO, Parent2's metA is called first (method overriding)
c1.metA()

# Calls metC; unique to Child
c1.metC()