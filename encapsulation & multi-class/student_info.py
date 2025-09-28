class Student:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    def details(self):
        print(f"Name:", self.__name)
        print(f"ID:",self.__id)

    def set_ID(self, ID):
        if ID < 0:
            print(f"Invalid!")
        else:
            self.__id = ID
    def get_ID(self):
        return self.__id

    def set_name(self, Name):
        self.__name = Name

    def get_name(self):
        return self.__name

s1 = Student("Jawad", 67)
s1.details()
print(f"------------------------------------------------")
s1.set_ID(99)
s1.set_name("Rahim")
s1.details()