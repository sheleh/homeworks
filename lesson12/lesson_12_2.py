#Library
#Write a class structure that implements a library. Classes:
#1) Library - name, books = [], authors = []
#2) Book - name, year, author (author must be an instance of Author class)
#3) Author - name, country, birthday, books = []
#Library class
#Methods:
#- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds
# the book to the books list for the current library.
#- group_by_author(author: Author) - returns a list of all books grouped by the specified author
#- group_by_year(year: int) - returns a list of all the books grouped by the specified year
#All 3 classes must have a readable __repr__ and __str__ methods.
#Also, the book class should have a class variable which holds the amount of all existing books


class Library:
    def __init__(self, lib_name):
        self.lib_name = lib_name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author, country, birthday):
        self.name = name
        self.year = year
        self.author = author
        self.country = country
        self.birthday = birthday
        self.nauthor = Author(self.author, self.country, self.birthday)
        #print(self.nauthor.name)
        if self.nauthor.name not in self.authors:
            self.authors.append(self.nauthor)
        else:
            print('Already in book')
        if self.name not in self.books:
            book = Book(self.name, self.year, self.nauthor)
            self.books.append([book])
    def __str__(self):
        return f'{self.lib_name} / {self.books} / {self.author}'

    def __repr__(self):
        return f'{self.lib_name} / {self.books} / {self.author}'

class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.name} / {self.year}/ {self.author} '

    def __repr__(self):
        return f'{self.name} / {self.year}/ {self.author} '

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
    def __str__(self):
        return f'{self.name} / {self.country}/ {self.birthday} '

    def __repr__(self):
        return f'{self.name} / {self.country}/ {self.birthday} '

lib = Library('Mylib')
lib.new_book('War and Peace', 1900, 'Tolstoy','Russia', 1828)
lib.new_book('Dead souls', 1835, 'Gogol','Russia', 1809)
lib.new_book('Night before Christmas', 1832, 'Gogol', 'Russia',1809)
print(lib)
print(lib.authors)
for i in lib.authors:
    print(i.name)
  
