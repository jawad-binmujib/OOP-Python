#########################  ENCAPSULATION  ################################

class car:

    def __init__(self, name , cc):
        self.__name = name         #<<<<<<<<<< private attribute <<<<<<<<<<
        self.__cc = cc             #<<<<<<<<<< private attribute <<<<<<<<<<
    def details(self):
        print(f"Name:",self.__name)
        print(f"CC:",self.__cc)
    def set_cc(self, Cc):
        if Cc < 0:
            print(f"Invalid")
        else:
            self.__cc = Cc

    def get_cc(self):
        return self.__cc

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name


c1 = car("AUDI", 2000)
c2 = car("AUDI", 2000)
c1.set_cc(2002)
c2.details()
c1.set_name("BMW")
c1.details()