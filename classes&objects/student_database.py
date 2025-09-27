class StudentDatabase:
    def __init__(self, student_name, student_id):
        self.name = student_name
        self.id = student_id
        self.grades = {}
    def calculateGPA(self, courses, semester):
        total_grades = []
        total_credit = 0
        total_point = 0
        for i in courses:
            course, grade = i.split(": ")
            grade = float(grade)
            total_point += grade * 3
            total_credit += 3
            total_grades.append(course)
        gpa = total_point / total_credit
        gpa="{:.2f}".format(gpa)
        if semester in self.grades:
          tuple1 = tuple(total_grades)
          semester_grade = self.grades[semester]
          semester_grade[tuple1] = gpa
        else:
          semester_grade = {}
          courses_tuple = tuple(total_grades)
          semester_grade[courses_tuple] = gpa
          self.grades[semester] = semester_grade
    def printDetails(self):
        print('Name:',self.name)
        print('ID:',self.id)
        for semester, grades_dict in self.grades.items():
            semester_grade = self.grades[semester]
            courses_tuple2 = list(semester_grade.keys())
            tuple2 = courses_tuple2[0]
            courses = list(tuple2)
            print('Courses taken in',semester)
            for i in courses:
                print(i)
            semester_grade = self.grades[semester]
            cgpa = list(semester_grade.values()) 
            gpa = cgpa[0]
            print("GPA:",gpa)


s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0','MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'],
'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7','ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()