class NikeBangladesh:
    branch_list = []
    total_sold = 0
    current_stock = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}


    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.branch_stock = {}
        for product, quantity in self.current_stock.items():
            self.branch_stock[product] = quantity
        NikeBangladesh.branch_list.append(branch_name)
        self.branch_sell = 0
    @classmethod
    def status(cls):
        print(f"Nike Bangladesh Status:")
        print(f"Branches Opened: {cls.branch_list}")
        print(f"Currently Stocked {cls.current_stock}")
        print(f"Sold: {cls.total_sold}")

    def details(self):
        print(f"Nike {self.branch_name} outlet")
        print(f"Products currently stocked:\n{self.branch_stock}")
        print(f"Sold: {self.branch_sell}")

    def restockProducts(self, name_quantity):
        for product , quantity in name_quantity.items():
            self.branch_stock[product] += quantity
            NikeBangladesh.current_stock[product] += quantity

    def productSold(self, name_quantity):
        for product, quantity in name_quantity.items():
            if quantity <= self.current_stock[product]:
                self.branch_stock[product] -= quantity
                NikeBangladesh.current_stock[product] -= quantity
                NikeBangladesh.total_sold += quantity
                self.branch_sell += quantity
            else:
                return f"Not enough {product} in stock to fulfill the order"

print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts({"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts({"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()

