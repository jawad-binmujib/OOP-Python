class Contacts:

    def __init__(self, names, numbers):
        self.names = names
        self.numbers = numbers
        self.contactDict = {}
        if len(names) != len(numbers):
            print(f"Contacts cannot be saved. Lenghth mismatched!")
            self.contactDict = {}
        else:
            self.contactDict = {}
            for i in range(len(names)):
                self.contactDict[names[i]] = numbers[i]
            print(f"Contacts saved successfully")
names = ["Emergency", "Father", "Bestie"]
numbers = ["999", "01xx23", "01xx87", "01xx65", "01xx43"]
m1 = Contacts(names, numbers)
print("Saved Contacts:", m1.contactDict)
print("---------------------------------------------")
names.append("Mother")
numbers.pop()
m2 = Contacts(names, numbers)
print("Saved Contacts:", m2.contactDict)

