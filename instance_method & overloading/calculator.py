class calculator:
    def product(self, num1, num2 = None, num3 = None):
        if num1 != None and num2 != None and num3 != None:
            print(num1*num2*num3)
        elif num1 != None and num2 != None:
            print(num1 * num2)
        else:
            print(1*num1)

int1 = calculator()
int1.product(6)
int1.product(6,8)

####but what if we take n number of arguments?? for that we need to use asterisk(*) so that we can take infinite number of arguments

class calculator:

    def __init__(self):
        pass
    def prod(self, *nums):
        pro = 1
        for i in nums:
            pro*= i
        print(f"product is:{pro}")
    def addition(self, *numb):
        sum = 0
        for j in numb:
            sum+=j
        print(f"summation is:{sum}")

    def subtraction(self, *num):
        subs= 0
        for x in num:
            subs = x - subs
        print(subs)



int2 = calculator()

int2.prod(5,6,7)
int2.addition(5,6,7)
int2.subtraction(5,6,7)
