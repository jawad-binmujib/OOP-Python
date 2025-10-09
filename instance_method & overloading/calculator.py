# The asterisk (*) allows the method to accept any number of arguments.
# This is useful when you don't know beforehand how many inputs the user will provide.

class Calculator:
    def product(self, num1, num2=None, num3=None):
        if num1 is not None and num2 is not None and num3 is not None:
            print(f"product is:{num1 * num2 * num3}")
        elif num1 is not None and num2 is not None:
            print(f"product is:{num1 * num2}")
        else:
            print(f"product is:{1 * num1}")

    def prod(self, *nums):
        pro = 1
        for i in nums:
            pro *= i
        print(f"product is:{pro}")

    def addition(self, *numb):
        sum = 0
        for j in numb:
            sum += j
        print(f"summation is:{sum}")

    def subtraction(self, *num):
        if not num:
            print("No numbers provided")
            return
        subs = num[0]
        for x in num[1:]:
            subs -= x
        print(f"subtraction is:{subs}")

# Usage
int1 = Calculator()
int1.product(6)
int1.product(6, 8)

print('----------------------------')

int2 = Calculator()
int2.prod(5, 6, 7)
int2.addition(5, 6, 7)
int2.subtraction(5, 6, 7)