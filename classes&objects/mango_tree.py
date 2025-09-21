class MangoTree:
    def __init__(self, variety, height = 1, number_of_mangoes = 0):
        self.variety = variety
        self.height = height
        self.number_of_mangoes = number_of_mangoes

mangoTree1= MangoTree("Gopalbhog")
mangoTree1.height = 16
mangoTree1.number_of_mangoes = 160
# Display the details of the mango tree
print(f"Updated details after 5 years:")
print("=====================================")
#print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
mangoTree2= MangoTree("Amrapali")
mangoTree2.height  = 16
mangoTree2.number_of_mangoes = 240
# Display the details of the mango tree
#print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")
