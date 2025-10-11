class Parent:
    def __init__(self, name, dob):
        # Initialize parent with name and date of birth
        self.name = name
        self.dob = dob

    def metA(self):
        print("metA is a method of Parent class ")

class Child(Parent):
    def __init__(self, name=None, dob=None, loc=None):
        # Initialize child, call parent constructor, add location
        super().__init__(name, dob) 
        self.loc = loc

    def metB(self):
        print("metB is a method of child class ")

# Create a Child object with default parameters
s1 = Child()
s1.metA()  # Inherited method from Parent
s1.metB()  # Method from Child