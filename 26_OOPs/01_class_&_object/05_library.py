

class Library:
    # totalBooks = 10
    # books = 
    def __init__(self):
        self.booksCount = 0
        self.books = []

    def addBooks(self,book):
        self.books.append(book)
        self.booksCount = len(self.books)

    def showInfo(self):
        print(f"Total books are present in the library is {self.booksCount}. The Books are   ")
        for book in self.books:
            print(book)    

j1 = Library()
j1.addBooks("Atomic habit")
j1.addBooks("Rich dad Poor dad")
j1.addBooks("The power of your subconcious mind")
j1.addBooks("The Art of War")
j1.addBooks("The psychology of money")
j1.addBooks("hyperfocus")
j1.addBooks("Miracle Morning")
j1.addBooks("Mindset")
j1.showInfo()
