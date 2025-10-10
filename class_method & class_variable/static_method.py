class Student:
    uni = "Bracu" # class variable
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def info(self):
        print(f"Name:",self.name)
        print(f"ID:",self.id)
        print(f"University Name:",Student.uni)
    @classmethod
    def change_uni(cls ,name):
        cls.uni = name
    @classmethod
    def string_name(cls, info):
        nam , id = info.split("_")
        obj = cls( nam , id)  # creating an object of that class
        return obj


    @staticmethod
    def check_dpt(id):
        if  id [3:5] == "01":
            print(f"CSE")
        elif id [3:5] == "41":
            print(f"CS")
s2  =  Student("Jawad",666)
Student.change_uni("Brac University")
s2.info()
Student.check_dpt("23141076")
s5 = Student.string_name("Jawad_23101076")
s5.info()
s5.check_dpt("23101076")