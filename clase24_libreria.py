from typing import Any

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"EL LIBRO {self.title} HA SIDO PRESTADO")
        else:
            print(f"EL LIBRO {self.title} NO ESTA DISPONIBLE ")

    def return_book(self):
        self.available = True
        print(f"EL LIBRO {self.title} CON EL NOMBRE HA SIDO DEVUELTO ")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"EL LIBRO {book.title} NO ESTA DISPONIBLE")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"EL LIBRO {book.title}NO ESTA EN LA LISTA DE PRESTADOS")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"EL LIBRO {book.title} HA SIDO AGREGADO")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"EL USUARIO {user.name} HA SIDO REGISTRADO")

    def show_available_books(self):
        print("LOS LIBROS DISPONIBLES: ")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")

#CREAR LOS LIBROS 
book1 = Book("EL PRINCIPITO", "ANTOINE DE SAINT-EXUPERY")
book2 = Book("1984", "GEORGE ORWELL")

#CREAR UN USUARIO 
user1 = User("CARLI", "001")

#CREAR LA BIBLIOTECA 
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

#MOSTAR LIBROS 
library.show_available_books()

#REALIZAR PRESTAMO
user1.borrow_book(book1)

#MOSTAR LIBROS 
library.show_available_books()

#DEVOLVER LIBRO
user1.return_book(book1)

#MOSTAR LIBROS 
library.show_available_books()