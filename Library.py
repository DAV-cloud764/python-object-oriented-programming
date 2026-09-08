from datetime import datetime, timedelta


# ============================================================
# BOOK
# ============================================================

class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self._available = True

    # ---------- Properties ----------

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Author must be a non-empty string.")
        self._author = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("ISBN must be a non-empty string.")
        self._isbn = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer.")
        self._year = value

    @property
    def available(self):
        return self._available

    # ---------- Behavior ----------

    def borrow(self):
        if not self.available:
            raise ValueError(
                f"'{self.title}' is currently not available."
            )

        self._available = False

    def return_book(self):
        if self.available:
            raise ValueError(
                f"'{self.title}' is already available in the library."
            )

        self._available = True

    # ---------- Dunder methods ----------

    def __str__(self):
        return (
            f"'{self.title}' by {self.author} "
            f"(ISBN: {self.isbn}, Year: {self.year})"
        )

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return self.isbn == other.isbn


# ============================================================
# USER
# ============================================================

class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Email must be a non-empty string.")
        self._email = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, int):
            raise ValueError("User ID must be an integer.")
        self._user_id = value

    def __str__(self):
        return (
            f"User: {self.name}, "
            f"Email: {self.email}, "
            f"ID: {self.user_id}"
        )


# ============================================================
# LOAN
# ============================================================

class Loan:
    def __init__(self, book, user):
        if not isinstance(book, Book):
            raise TypeError("book must be a Book object.")

        if not isinstance(user, User):
            raise TypeError("user must be a User object.")

        self.book = book
        self.user = user
        self.borrowed_date = datetime.now()
        self.due_date = self.borrowed_date + timedelta(days=14)

    def __str__(self):
        return (
            f"Loan: '{self.book.title}' "
            f"borrowed by {self.user.name} | "
            f"Borrowed: {self.borrowed_date.strftime('%Y-%m-%d')} | "
            f"Due: {self.due_date.strftime('%Y-%m-%d')}"
        )


# ============================================================
# LIBRARY
# ============================================================

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    # ---------- Book management ----------

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added.")

        if self.find_book(book.isbn) is not None:
            raise ValueError(
                f"A book with ISBN {book.isbn} already exists."
            )

        self.books.append(book)

    def remove_book(self, isbn):
        book = self.find_book(isbn)

        if book is None:
            raise ValueError(
                f"Book with ISBN {isbn} was not found."
            )

        if not book.available:
            raise ValueError(
                "Cannot remove a book that is currently borrowed."
            )

        self.books.remove(book)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book

        return None

    def list_books(self):
        if not self.books:
            print("The library has no books.")
            return

        for number, book in enumerate(self.books, start=1):
            status = "Available" if book.available else "Borrowed"

            print(
                f"{number}. {book} | Status: {status}"
            )

    # ---------- User management ----------

    def add_user(self, user):
        if not isinstance(user, User):
            raise TypeError("Only User objects can be added.")

        if self.find_user(user.user_id) is not None:
            raise ValueError(
                f"User with ID {user.user_id} already exists."
            )

        self.users.append(user)

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user

        return None

    # ---------- Loan management ----------

    def borrow_book(self, isbn, user):
        if not isinstance(user, User):
            raise TypeError("user must be a User object.")

        book = self.find_book(isbn)

        if book is None:
            raise ValueError(
                f"Book with ISBN {isbn} was not found."
            )

        # Book controls its own availability.
        book.borrow()

        # Library creates and owns the transaction.
        loan = Loan(book, user)

        self.loans.append(loan)

        return loan

    def return_book(self, isbn):
        book = self.find_book(isbn)

        if book is None:
            raise ValueError(
                f"Book with ISBN {isbn} was not found."
            )

        # Book controls its own state.
        book.return_book()

        # Find the active loan associated with this book.
        for loan in self.loans:
            if loan.book.isbn == isbn:
                self.loans.remove(loan)
                return

        raise ValueError(
            f"No active loan was found for ISBN {isbn}."
        )

    def list_loans(self):
        if not self.loans:
            print("There are no active loans.")
            return

        for number, loan in enumerate(self.loans, start=1):
            print(f"{number}. {loan}")


# ============================================================
# APPLICATION / TEST
# ============================================================

book1 = Book(
    "Clean Code",
    "Robert C. Martin",
    "9780132350884",
    2008
)

book2 = Book(
    "The Great Gatsby",
    "F. Scott Fitzgerald",
    "9780743273565",
    1925
)

user1 = User(
    "David Francis",
    "francis@gmail.com",
    1
)

user2 = User(
    "John Doe",
    "john@example.com",
    2
)


library = Library()

# Add books
library.add_book(book1)
library.add_book(book2)

# Add users
library.add_user(user1)
library.add_user(user2)

print("\n===== BOOKS =====")
library.list_books()

print("\n===== BORROW =====")

loan = library.borrow_book(
    book1.isbn,
    user1
)

print(loan)

print("\nBook availability:")
print(book1.available)

print("\n===== ACTIVE LOANS =====")
library.list_loans()

print("\n===== BOOKS AFTER BORROWING =====")
library.list_books()

print("\n===== RETURN =====")

library.return_book(book1.isbn)

print("Book availability:")
print(book1.available)

print("\n===== ACTIVE LOANS AFTER RETURN =====")
library.list_loans()

print("\n===== BOOKS AFTER RETURN =====")
library.list_books()