class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")


my_library = Library()

book_0 = Book("To Kill a Mockingbird", "Harper Lee")
book_1 = Book("The Great Gatsby", "F.Scott Fitzgerald")
my_library.add_book(book_0)
my_library.add_book(book_1)
my_library.list_books()

