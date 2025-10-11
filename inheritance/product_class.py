class Product:
    def __init__(self, id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price

    def get_id_title_price(self):
        # Return product details
        return f"ID: {self.__id} Title: {self.__title} Price: {self.__price}"

class Book(Product):
    def __init__(self, id, title, price, isbn=None, publisher=None):
        super().__init__(id, title, price)
        self.isbn = isbn
        self.publisher = publisher

    def printDetail(self):
        # Return details including Book-specific attributes
        return f"{self.get_id_title_price()}\nISBN: {self.isbn} Publisher: {self.publisher}"

class CD(Product):
    def __init__(self, id, title, price, band=None, duration=None, genre=None):
        super().__init__(id, title, price)
        self.band = band
        self.duration = duration
        self.genre = genre

    def printDetail(self):
        # Return details including CD-specific attributes
        return f"{self.get_id_title_price()}\nBand: {self.band} Duration: {self.duration} minutes\nGenre: {self.genre}"


book = Book(1, "The Alchemist", 500, "97806", "HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2, "Shotto", 300, "Warfaze", 50, "Hard Rock")
print(cd.printDetail())