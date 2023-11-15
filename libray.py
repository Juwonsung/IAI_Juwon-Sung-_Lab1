from book_info import book_lists
from customer import Customer
from book import Book


class Library(Book, Customer): # class inheritance
    # ADD BOOKS
    def add_books(self, title, author, ISBN, status):
        book_list = []
        books = {}
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.status = status
        books["title"] = self.title
        books["author"] = self.author
        books["ISBN"] = self.ISBN
        books["status"] = self.status
        book_list.append(books)
        book_lists.append(books)

    #register customer is from customer.py

    def book_showing(self):
        print("<available book lists>")
        for book in book_lists:
            if book["status"] == "available":
                print(f"title : {book['title']} status: {book['status']} ")
# define class
library = Library()

# book management
customer_info = library.regis_customer("juwon",23)
library.book_showing()
want_book = library.book_manag()
print(f"customer : {customer_info} \nbook Lists : {want_book}")

library.add_books("AI", "Heinrich", "1234567890", "available")
library.book_showing()