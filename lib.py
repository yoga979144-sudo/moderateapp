class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[{status}] {self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def show_books(self):
        print("\n--- Library Inventory ---")
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                print(f"Success! You have borrowed '{book.title}'.")
                return
        print("Sorry, book is either unavailable or doesn't exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.is_available = True
                print(f"Success! You have returned '{book.title}'.")
                return
        print("Error: Could not return this book.")

# --- Execution Example ---
my_library = Library()

# Populate library
my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "12345"))
my_library.add_book(Book("1984", "George Orwell", "67890"))

# Interaction
my_library.show_books()
my_library.borrow_book("1984")
my_library.show_books()
my_library.return_book("1984")