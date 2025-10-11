class KKTea:
    sale_dict = {}
    def __init__(self, price, t_bag=50, name='Regular'):
        self.price = price
        self.t_bag = t_bag
        self.name = f"KK {name} Tea"
        self.weight = 2 * self.t_bag
        self.status = False
        KKTea.sale_dict[self.name] = 0

    def product_detail(self):
        print(f"Name: {self.name}, Weight: {self.weight} \nTea Bags: {self.t_bag}, Price: {self.price} \nStatus: {self.status}")

    @classmethod
    def total_sales(cls):
        print(f"Total Sales: {cls.sale_dict}")

    @classmethod
    def update_sold_status_regular(cls, *amount):
        for i in amount:
            i.status = True
            cls.sale_dict[i.name] += 1

class KKFlavouredTea(KKTea):
    def __init__(self, name, price, t_bag):
        super().__init__(price, t_bag, name)

    @classmethod
    def update_sold_status_flavoured(cls, *amount):
        for i in amount:
            i.status = True  
            cls.sale_dict[i.name] += 1

# Demonstration code
t1 = KKTea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KKTea.total_sales()
print("-----------------3-----------------")
t2 = KKTea(470, 100)
t3 = KKTea(360, 75)
KKTea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KKTea.total_sales()
print("-----------------6-----------------")
t4 = KKFlavouredTea("Jasmine", 260, 50)
t5 = KKFlavouredTea("Honey Lemon", 270, 45)
t6 = KKFlavouredTea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KKFlavouredTea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KKTea.total_sales()