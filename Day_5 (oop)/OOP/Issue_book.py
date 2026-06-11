class Book:
  def __init__(self, title, author):
    self.title = title        # ClassName.ObjName = Variable
    self.author = author
    self.available = True
    
  def issue_book(self):
    if self.available:
      self.available = False
      print(f'\n{self.title}" has been issued')
    else:
      print(f'\n{self.title}" is already issued')

  def return_book(self):
    self.available = True
    print(f'\n{self.title}" has been returned')

  def display(self):
    status = "Available" if self.available else "Issued"
    print(f"Title : {self.title}")
    print(f"Author : {self.author}")
    print(f"Status : {status}")

book1 = Book("Python Programming", "John smith")
book1.display()
book1.issue_book()
book1.display()
book1.return_book()
book1.display()