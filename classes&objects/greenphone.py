class GreenPhone:
    def __init__(self, model_name, android_version, numb_of_camera):

        self.company_name = "GreenPhone"
        self.model_name = model_name
        self.android_version = android_version
        self.number_of_camera = numb_of_camera
        if self.model_name[0] == 'A':
            self.max_version = self.android_version + 2
        elif self.model_name[0] == 'M':
            self.max_version = self.android_version + 3
        elif self.model_name[0] == 'U':
            self.max_version = self.android_version + 4
    def showSpecification(self):
        print(f"Phone Company: {self.company_name}")
        print(f"Model Name: {self.model_name}")
        print(f"Android Version: {self.android_version}")
        print(f"Number Of Cameras: {self.number_of_camera}")

    def updatePhone(self):
        if self.android_version < self.max_version:
            self.android_version+=1
            print(f"Your phone {self.company_name} {self.model_name} is upgraded to Android Version: {self.android_version}")
        else:
            print(f"Your phone {self.company_name} {self.model_name} is already up to date")



print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()
