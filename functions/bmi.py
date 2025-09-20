def bmi(h,w):
    h= h/ 100
    b = w/(h**2)
    if b > 30:
        print(f'score is {b:.1f}. You are Obese')
    elif 25<=b<=30:
        print(f'score is {b:.1f}. you are Overweight')
    elif 18.5<=b<=24.9:
        print(f'score is {b:.1f}. you are Normal')
    else:
        print(f'score is {b:.1f}. you are Underweight')
bmi(152,48)