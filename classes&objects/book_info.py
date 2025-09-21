############################## HOMEWORK ##############################
import datetime

class Book:
    def __init__(self, name, author, year_of_publication):
        self.name = name
        self.author = author
        self.year_of_publication = year_of_publication
        self.status = self.status()
        print(f"Chechking the book.")
    def status(self):
        today = datetime.date.today()
        year = today.year
        difference = year - self.year_of_publication
        if difference >= 400:
            return "Accepted. The book is stored on floor: 2"
        elif difference >= 200:
            return "Accepted. The book is stored on floor: 1"
        elif difference > 100:
            return "Accepted. The book is stored on floor: 0"
        else:
            return "Rejected. The book is not enough antique"

book1 = Book('The Act', 'Ferguson', 1924)
print(f"{book1.author} wrote the book '{book1.name}'.")
print(f"This book was published in {book1.year_of_publication}.")
print(f"This book is {book1.status}")
print("-------------------------------------")
book2 = Book('Flame', 'Nolan', 1932)
print(f"{book2.author} wrote the book '{book2.name}'.")
print(f"This book was published in {book2.year_of_publication}.")
print(f"This book is {book2.status}")
print("-------------------------------------")
book3 = Book('Norms', 'Alfred', 1832)
print(f"{book3.author} wrote the book '{book3.name}'.")
print(f"This book was published in {book3.year_of_publication}.")
print(f"This book is {book3.status}")
print("-------------------------------------")
book4 = Book('Apex', 'Samson', 1923)
print(f"{book4.author} wrote the book '{book4.name}'.")
print(f"This book was published in {book4.year_of_publication}.")
print(f"This book is {book4.status}")
print("-------------------------------------")
book5 = Book('Habitat', 'Eden', 1723)
print(f"{book5.author} wrote the book '{book5.name}'.")
print(f"This book was published in {book5.year_of_publication}.")
print(f"This book is {book5.status}")
print("-------------------------------------")
book6 = Book('Apocalypto', 'Menez', 1603)
print(f"{book6.author} wrote the book '{book6.name}'.")
print(f"This book was published in {book6.year_of_publication}.")
print(f"This book is {book6.status}")
