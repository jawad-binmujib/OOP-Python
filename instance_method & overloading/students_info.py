class Student:
    def __init__(self, name, student_id, cgpa):
        self.name = name
        self.student_id = student_id
        self.cgpa = cgpa
    def setId(self, new_id):
        self.student_id = new_id
class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
    def findStudent(self, student_id):
        found = False
        for student in self.students:
            if student.student_id == student_id:
                print("Student info:")
                print("Student Name:", student.name)
                print("ID:", student.student_id)
                print("CGPA: ", student.cgpa)
                found = True
                break
        if not found:
            print("Student with this ID doesn't exist, Please give a valid ID")
    def addStudent(self, *students):
        for student in students:
            exists = False
            for existing_student in self.students:
                if existing_student.student_id == student.student_id:
                    print("Student with the same ID already exists, Please try with another ID")
                    exists = True
                    break
            if not exists:
                self.students.append(student)
                print("Welcome to", self.name, "department,", student.name)
    def details(self):
        print("Department Name:", self.name)
        print("Number of student:", len(self.students))
        print("Details of the students:")
        for student in self.students:
            print("Student name:", student.name, ", ID:", student.student_id, ", cgpa:", student.cgpa)
# Driver Code
s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1, s2, s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib", 22301010, 3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib", 22201010, 2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()