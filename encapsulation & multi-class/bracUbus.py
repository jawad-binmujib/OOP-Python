#task5
class BracUStudent:
  def __init__(self,student_name ,home):
    self.student_name =student_name
    self.home=home
    self.bus_pass= False
  def show_details(self):
    print(f"Student Name : {self.student_name}" )
    print(f"Lives in {self.home}")
    print(f"Have Bus Pass? {self.bus_pass}")
  def get_pass(self):
      self.bus_pass= True
class BracUBus:
  def __init__(self,route,capacity=2):
    self.route = route
    self.capacity=capacity
    self.count=0
    self.student_list=[]
  def show_details(self):
    print(f"Bus Route:{self.route}")
    print(f"Passengers Count: {self.count} Max: {self.capacity}")
    print(f"Passengers On Board: {self.student_list}")
  def board(self,*student):
    if len(student)==0:
      print(f"No passengers!")
    for i in student:
      if self.count<self.capacity:
        if i.bus_pass==False:
          print(f"You don't have a bus pass!")
        elif i.home!=self.route:
          print(f"You got on the wrong bus!")
        else:
          print(f"{i.student_name} boarded the bus.")
          self.student_list.append(i.student_name )
          self.count+=1
      else :
        print(f"Bus is full!")
st1 = BracUStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracUStudent("Shanto", "Motijheel")
st3 = BracUStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracUBus("Mirpur")
bus2 = BracUBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()