class Student:
    def __init__(self, name, id, dept = "CSE"):
        self.name = name
        self.id = id
        self.dept = dept
    def dailyEffort(self, hour):
        self.hour = hour
        self.sugg = " "
        if self.hour <= 2:
            self.sugg+="Should Give More Effort!"
        elif self.hour <= 4:
            self.sugg+="Keep Up The Good Work!"
        else:
            self.sugg+="Excellent! Now motivate others."
    def printDetails(self):
        print(f"Name:", self.name)
        print(f"ID:", self.id)
        print(f"Department:", self.dept)
        print(f"Daily Effort: {self.hour} hours(s)" )
        print(f"Suggestion:",self.sugg)

harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
