#task-04
class Shopidify:
  def __init__(self,name=""):
    self.name=name
    print("Welcome",name,"to Shopidify ")
    if self.name=="":
      self.name="Guest"
    self.cart={}
    self.trans=0
  def add_to_cart(self,item,quantity=1):
    if type(item)!=list:
      if item not in self.cart:
        self.cart[item]=quantity
      else:
        self.cart[item]+=quantity
    else:
      for i in range(len(item)):
        if i%2==0:
          if item[i] not in self.cart:
            self.cart[item[i]]=item[i+1]
          else:
            self.cart[item[i]]+=item[i+1]
  def display_cart(self):
    print("Items in the cart for",self.name,":")
    for item,quantity in self.cart.items():
      print(f"- {item} : {quantity}x")
  def checkout(self):
    print(f"Checkout completed for {self.name}:")
    self.trans+=1
  def display_history(self):
    print(f"Purchase history for {self.name}:")
    for i in range(self.trans):
      print(f"Transaction {i+1}:")
      for item,quantity in self.cart.items():
        print(f"- {item} : {quantity}x")

guest_account = Shopidify()
print("1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account = Shopidify("John")
print("2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan", 2)
guest_account.add_to_cart("Luffy Action Figure")
guest_account.display_cart()
print("3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.add_to_cart(["Chocolate Chip Cookies", 3,"Goku Action Figure",2,"Dumbbells-5kg",2])
john_account.display_cart()
print("4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan")
guest_account.display_cart()
print("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.checkout()
print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.display_history()
print("7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.checkout()
print("8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.display_history()
print("9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")