class Student:
    uni_name = "BracU" # class variable
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print(f"Name:",self.name)
        print(f"ID:",self.id)
        print(f"Uni Name:",self.uni_name)
    @classmethod
    def update_uni_name(cls, uni_name):
        cls.uni_name = uni_name


s1 = Student("Jawad" ,11)
s2 = Student("Nahiyan", 22)
s1.details()
s2.details ()
print(f"----------------------------------------------------------------------")
Student.update_uni_name("Brac University")
s1.details()
s2.details()

print(f"----------------------------------------------------------------------")
print(f"classmethod without an object")
print(f"\n")
class Student:
    uni_name = "BracU"
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print(f"Name:",self.name)
        print(f"ID:",self.id)
        print(f"Uni Name:",self.uni_name)
    @classmethod
    def update_uni_name(cls, uni_name):
        cls.uni_name = uni_name
        print("Class method has been created!")
        print("Class method has been created!")

Student.update_uni_name("Brac University")
