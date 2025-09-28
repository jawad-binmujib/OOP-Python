class Library:
  def __init__(self,place,dict1):
    self.place=place
    self.book_quantity=dict1 # dictionary of {category: quantity}
    self.borrower={}         # tracks total books borrowed per reader
  def details(self):
    print(f"{self.place} Library details\nBorrower details:\n{self.borrower}\nBooks availability:\n{self.book_quantity}")
class Reader:
  def __init__(self,reader_name ):
    self.reader_name =reader_name
    self.count=0
    self.books={}  # tracks borrowed books per category
  def borrow(self,*infos):
    library=infos[0]
    for i in range(1,len(infos)):
      if library.book_quantity[infos[i]]!=0:
        if self.count<5:
          print(f"{infos[i]} book is borrowed successfully")
          self.count+=1
          library.book_quantity[infos[i]]-=1
          if infos[i] not in self.books:
            self.books[infos[i]]=1
          else:
            self.books[infos[i]]+=1
        else:
          print("You cannot borrow more than 5 books.")
      else:
        print(f"{infos[i]} books are not available at the moment.")
    library.borrower[self.reader_name ]=self.count
  def readerInfo(self,category=None):
    if category==None:
      print(f"{self.reader_name } you have {self.count} book(s) with you.")
      for category,quantity in self.books.items():
        print(f"Books on {category}:{quantity}")
    else:
      print(f"{self.reader_name }, you have {self.books[category]} {category} book(s) with you")


L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
r1=Reader('Aladdin')
r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1,'Politics','Fiction') # tests limits and availability
print("3----------------------")   
r1.readerInfo()                    # shows all books borrowed
print("4----------------------")
r1.readerInfo('Fiction')           # shows only Fiction
print("5----------------------")
L1.details()
print("6----------------------")
r2=Reader('Jasmine')
r2.borrow(L1,'Politics','Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()