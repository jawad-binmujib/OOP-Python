class Foodie:
 def __init__(self,name):
    self.name=name
    self.items=[]
    self.total=0
 def show_orders(self):
    return (f"{self.name} has {len(self.items)} items(s) in the cart\nItems: {self.items}\nTotal spent: {self.total}")
 def order(self,*infos):
    price=0
    for i in infos:
      item,quantity=i.split("-")
      price = menu[item]
      total=int(quantity)*price
      self.total+=total
      self.items.append(item)
      print(f"Ordered - {item}, quantity - {quantity}, price (per Unit) - {price}. \nTotal price - {self.total}")
 def pay_tips(self,amount=0):
    self.total+=amount
    if amount==0:
      print("No tips to the waiter.")
    else:
      print("Gives",amount," /- tips to the waiter.")
menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}


f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())