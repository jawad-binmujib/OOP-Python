class Department:
  def __init__(self,dept="ChE Department",sec=5):
    self.dept=dept
    self.sec=sec
    self.avg=0
    self.objects=[]
    print(f"The {dept} has {sec} sections.")
  def add_students(self,*students):
    if len(students)==self.sec:
      sum=0
      for i in students:
        sum+=i
      avg=sum/len(students)
      self.avg+=avg
      print(f"The {self.dept} has an average of {avg} students in each section")
    else:
      print(f"The {self.dept} doesn't have {len(students)} sections")
  def merge_Department(self,*objects):
    sum=0
    for obj in objects:
      if obj not in self.objects:
        print(f"{obj.dept} is merged to {self.dept}.")
      self.objects.append(obj)
    for obj in self.objects:
      sum+=obj.avg*obj.sec
    sum1=self.avg*self.sec+sum
    avg=sum1/self.sec
    return(f"Now the {self.dept} has an average of {avg} students in each section.")
d1 = Department()
print('1-----------------------------')
d2 = Department('MME Department')
print('2-----------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------')
print(mega.merge_Department(d3))