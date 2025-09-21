
def calcu(days):
    i = days//365
    x = (days%365)//30
    k = (days%365)%30
    print(f"{i} Years, {x} Months, {k} Days")

calcu(400)

