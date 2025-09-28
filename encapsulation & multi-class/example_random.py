class MyClass:
    def __init__(self):
        self.__private_variable = 10

    def get_private_variable(self):
        return self.__private_variable


class AnotherClass:
    def __init__(self):
        self.obj = MyClass()

    def access_private_variable(self):
        private_var = self.obj.get_private_variable()
        print("Private variable value:", private_var)

# Usage
another_obj = AnotherClass()
another_obj.access_private_variable()  # Accessing private attribute via public method