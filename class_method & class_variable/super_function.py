class A:
    def __init__(self):
        print(f"Init method has been created!")

    def method1(self):
        print(f"You have to study 24/7")

    def method2(self):
        print(f"You will shine in life!")

class B(A):
    def __init__(self):
        # If you want to run the parent's __init__, you can use super().__init__() 
        pass

    def method2(self):
        super().method2()  # Calls the parent version of method2
        print(f"Method 2 has been created!")  # Child's additional behavior

m1 = B()
m1.method1()  # Inherited from class A
m1.method2()  # Overridden in class B, calls both parent and child versions