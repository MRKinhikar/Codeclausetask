class Library:
    def _init_(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.noBooks} books. The Books are")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Harry Potter and the Philosopher's Stone")
l1.addBook("Harry Potter and the Chamber od Secrets")
l1.addBook("Harry Potter and the Prisoner of Azkaban")
l1.showInfo()