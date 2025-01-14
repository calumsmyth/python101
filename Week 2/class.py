#Build a Simple Library System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    def __str__(self):
        return f"Book Title: {self.title}, Author: {self.author}"

class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []
    def __str__(self):
        return f"Member Name: {self.name}, Member ID: {self.id}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, book, member):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print(f"{book.title} has been lent to {member.name}.")
        else:
            print(f"Sorry {book.title} is unavailable to borrow")

    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"{book.title} has been returned by {member.name}")
        else:
            print(f"{member.name} did not borrow {book.title}")
    

#create books
book1= Book("Harry Potter", "J. K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

#Create Members
member1 = Member("John", 101)
member2 = Member("Alice", 102)

#create library
library = Library()

#add books to library
library.add_book(book1)
library.add_book(book2)

#add members
library.register_member(member1)
library.register_member(member2)

#test lending and returning books
#library.lend_book(book1,member1)
library.lend_book(book1, member1)
library.lend_book(book1, member2)



