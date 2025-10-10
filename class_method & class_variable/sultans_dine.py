class SultansDine:
    total_numb_of_branch = 0
    total_sell = 0
    branch_list = []

    def __init__(self,  branch_name):
        self.branch_name = branch_name
        SultansDine.branch_list.append(self)
        SultansDine.total_numb_of_branch += 1
        self.branch_sell = 0

    def branchInformation(self):
        print(f"Branch Name: {self.branch_name}")
        print(f"Branch Sell : {self.branch_sell}")
    def sellQuantity(self, amount):
        self.amount = amount 
        if amount < 10:
            self.branch_sell = amount * 300
        elif amount < 20:
            self.branch_sell = amount * 350
        else:
            self.branch_sell = amount * 400
        SultansDine.total_sell += self.branch_sell

    @classmethod
    def details(cls):
        print(f"Total Number of branch(s):{cls.total_numb_of_branch}")
        print(f"Total Sell:{cls.total_sell}")

        for i in SultansDine.branch_list:
            sell_percentage = (i.branch_sell/cls.total_sell)*100
            print(f"Branch Name:{i.branch_name}, Branch Sell:{i.branch_sell}\nBranch consists of total sell:{sell_percentage:.2f}%")

SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()


