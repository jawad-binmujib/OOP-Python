
def total_price(burger,loc = 'mohakhali'):

    #dc = 0
    if loc == "":
        dc = 40
    else:
        dc =  60
    if burger=="BBQ CC Burger":
        total_price = 250+ dc +(250*0.08)
    elif burger == "Beef Burger":
        total_price = 170+ dc +(170*0.08)
    elif burger == "Naga Drums":
        total_price = 200 + dc + (200*0.08)
    print(total_price)
burger = input()
loc = input()
total_price(burger,loc)
