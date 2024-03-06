'''Create a Python class named Book with the following attributes:

title (string)
author (string)
publication_year (integer)
genre (string)

Include methods in the class to:
Check if the book is a classic (published before 1900).
Print the book details.'''

class Book:
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    def classic(self):
        if self.publication_year < 1900:
            print("The book is a classic")
            return True
        else:
            print("The book is not considered a classic")
            return False

    def print_details(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Publication year: ", self.publication_year)
        print("Genre:", self.genre)

book1 = Book("Moby Dick", "Herman Melville", 1851, "Adventure fiction")
book1.classic()
book1.print_details()
