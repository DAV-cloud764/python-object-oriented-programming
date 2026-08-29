from datetime import datetime, timedelta

class books:
    def __init__(self, title, author, isbn, year, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = available

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError("Author must be a string.")
        self._author = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        if not isinstance(value, str):
            raise ValueError("ISBN must be a string.")
        self._isbn = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer.")
        self._year = value

    def __eq__(self, other):
        if not isinstance(other, books):
            return NotImplemented

        return self.isbn == other.isbn

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}, Year: {self.year})"       


    def borrow(self):
        if not self.available:
            print(f"Sorry, '{self.title}' by {self.author} is currently not available.")
        return
    
        self.available = False
        print(f"You have borrowed the book. '{self.title}' by {self.author}.")

    def return_book(self):
        if self.available:
            print(f"'{self.title}' by {self.author} is already returned in the library.")
        return
        self.available = True
        print(f"The book is returned '{self.title}' by {self.author}.")
   

book1 = books("Clean code", "Ngungi wa Thiongo", "9780743273565", 1976)
book2 = books("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)
 

class Library:
    def __init__(self, book):
        self.Book = []

    def add_book(self, book):
        self.Book.append(book)

    def remove_book(self, isbn):
        for book in self.Book:
            if book.isbn == isbn:
                self.Book.remove(book)
                break
        else:
            print(f"'{book.isbn}' by {book.author} is not in the library.") 

    def find_book(self, isbn):
        for book in self.Book:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        for book in self.Book:
            print(book)

class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}, ID: {self.user_id}"

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value  

    @property
    def email(self):
        return self._email


    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise ValueError("Email must be a string.")
        self._email = value 

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, int):
            raise ValueError("User ID must be an integer.")
        self._user_id = value


user = User("David Francis", "Francis@gmail.com", 1)
print(user)

class Loan:
    def __init__(self, book, user):
        self.book = book
        self.user = user
        self.borrowed_date = datetime.now()
        self.due_date = self.borrowed_date + timedelta(days=14)

    def __str__(self):
        return f"Loan: {self.book.title} borrowed by {self.user.name}, Due date: {self.due_date.strftime('%Y-%m-%d')}"

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, books):
            raise ValueError("Book must be an instance of the books class.")
        self._book = value    

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise ValueError("User must be an instance of the User class.")
        self._user = value

    @property
    def borrowed_date(self):
        return self._borrowed_date

    @borrowed_date.setter
    def borrowed_date(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Borrowed date must be a datetime object.")
        self._borrowed_date = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Due date must be a datetime object.")
        self._due_date = value

loan = Loan(book1, user)
print(loan)                               



library = Library([book1, book2])   
library.add_book(books("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960))
library.add_book(books("1984", "George Orwell", "9780451524935", 1949))

library.list_books()

found = library.find_book(book1.isbn)
if found:
    print(f"Found: {found}")
else:
    print(f"Book with ISBN {book1.isbn} not found.")

library.remove_book("9780743273565")
library.list_books()


