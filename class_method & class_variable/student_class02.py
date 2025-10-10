class Student:
    uni_name = "Bracu"

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.id}")
        print(f"Uni: {Student.uni_name}")

    @classmethod
    def update_un_name(cls, varsity_name):
        cls.uni_name = varsity_name

    @classmethod
    def from_string(cls, info):   
        name, id_numb = info.split("-") # passing two info with a single parameter using split("-")
        return cls(name, int(id_numb))  # convert id to int


s1 = Student.from_string("Karim-22") 
s2 = Student.from_string("Rahim-33")

s1.details()
Student.update_un_name("Brac University")
s2.details()
s1.details()
