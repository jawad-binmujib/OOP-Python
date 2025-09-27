class Student:
    def __init__(self, student_name, student_id, Dept = "CSE"):
        self.name = student_name
        self.id = student_id
        self.dept = Dept

    def dailyEffort(self, hour):
        self.hour = hour

    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Department: {self.dept}")
        print(f"Daily Effort: {self.hour}")
        if self.hour <= 2:
            print(f"Should give more effort!")
        elif self.hour <= 4:
            print(f"Keep up the good work!")
        else:
            print(f"Excellent ! Now motivate others")


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

