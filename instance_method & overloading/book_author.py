#task-05
class Author:
  def __init__(self,name=None):
    self.name=name
    self.book={}
    self.count=0
  def addBook(self,book,cate):
    if self.name==None:
      print("A book can not be added without author name ")
    else:
      if cate in self.book:
        self.book[cate].append(book)
        self.count+=1
      else:
        self.book[cate]=[]
        self.book[cate].append(book)
        self.count+=1
  def setName(self,name):
    self.name=name
  def printDetail(self):
    print(f"Number of Book(s): {self.count}\nAuthor Name: {self.name}")
    for cate,books in self.book.items():
      s=""
      for i in range(len(books)):
        if i!=len(books)-1:
          s+=books[i]+","
        else:
          s+=books[i]
      print(cate,":",s)
a1 = Author()
print("=================================")
a1.addBook("Ice", "Science Fiction")
print("=================================")
a1.setName("Anna Kavan")
a1.addBook("Ice", "Science Fiction")
a1.printDetail()
print("=================================")
a2 = Author("Humayun Ahmed")
a2.addBook("Onnobhubon", "Science Fiction")
a2.addBook("Megher Upor Bari", "Horror")
print("=================================")
a2.printDetail()
a2.addBook("Ireena", "Science Fiction")
print("=================================")
a2.printDetail()
print("=================================")
