class Order:
    def __init__(self, dict1, str1):
        self.items = self.order_details(dict1, str1)
    def order_details(self, dict1, str1):
        items = []
        total = 0
        for i in str1.split(', '):
            item, quantity = i.split('-')
            price = dict1[item] * int(quantity)
            items.extend([item, int(quantity), price])
            total += price
        items.append(total)
        return items[:-1]
# Write your class code here
dict1 = {'Chicken_Cheeseburger' : 249,'Mega_Cheeseburger' : 289,'Fries' : 139,'Hot_Wings' : 99,'Rice_Bowl' : 299,'Soft_Drinks' : 50}
order1 = Order(dict1, "Chicken_Cheeseburger-2, Fries-3, Soft_Drinks-3")
print(order1.items)
print()
print('-'*35)
print('Item           x Quantity :   Price')
print('--------------   --------   -------')
index = 0
total = 0
while index < len(order1.items):
  item = order1.items[index]
  quantity = order1.items[index+1]
  price = order1.items[index+2]

  print(f'{item:20} x {quantity:2} : {price:7.2f}')
  total += price
  index += 3 # Going to next item
print('-'*35)
print(f'Total:                      {total:7.2f}')
print('-'*35)