class Student:
    def __init__(self, name='Just a student', dept='nothing'):
        self.__name = name         # Private attribute
        self.__department = dept   # Private attribute

    def set_department(self, dept):
        self.__department = dept

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def detail(self):
        # Use f-string for better readability
        return f'Name: {self.__name} Department: {self.__department}'

class BBA_Student(Student):
    def __init__(self, name="default", dept="BBA"):
        # Inherit Student and set default department to "BBA"
        super().__init__(name, dept)

print(BBA_Student().detail())
print(BBA_Student('Humpty Dumpty').detail())
print(BBA_Student('Little Bo Peep').detail())