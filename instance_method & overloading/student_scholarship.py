class Student:
    def __init__(self, name, cg, cred = 9,dept = 'CSE'):
        self.name = name
        self.cgpa = cg
        self.dept = dept
        self.credit = cred

    def checkScholarshipEligibility(self):
        self.scholarship_status = ""
        if 3.5<= self.cgpa < 3.7 and self.credit >=10:
            print(f"{self.name} is eligible for Need-based scholarship")
            self.scholarship_status+="Need-based scholarship"
        elif self.cgpa >= 3.7 and self.credit >= 10:
            print(f'{self.name} is eligible for Merit-based scholarship')
            self.scholarship_status+="Merit-based scholarship"
        else:
            print(f"{self.name} is not eligible for scholarship")
            self.scholarship_status+="No scholarship"
    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.dept}")
        print(f"CGPA: {self.cgpa}")
        print(f"Number of credits: {self.credit}")
        print(f"Scholarship status: {self.scholarship_status}")


print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()
