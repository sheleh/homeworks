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

    def new_book(self, name, year, author):

        book = Book(name, year, author)
        self.books.append(book)

        author.add_book(name) ### тут засада
        self.authors.append(author) ## и тут

    def group_by_author(self, author):
        res = '/'
        for au in self.authors:
            if au.fullname == author:
                res += au.books[0] + ' /'
        return res

    def group_by_year(self, year):
        res = '/'
        for item in self.books:
            if item.year == year:
                res += str(item.name)
        return res

    def __str__(self):
        return f'{self.lib_name} / {self.books} / '

    def __repr__(self):
        return f'{self.lib_name} / {self.books} / '

class Book:
    b_count = 0  # количество всех книг
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.b_count += 1


    def __str__(self):
        return f'{self.name} / {self.year}/ {self.author} '

    def __repr__(self):
        return f'{self.name} / {self.year}/ {self.author} '

class Author:
    def __init__(self, fullname, country, birthday):
        self.fullname = fullname
        self.country = country
        self.birthday = birthday
        self.books = []
    def add_book(self, name):
        self.books.append(name)
    def __str__(self):
        return f'{self.fullname} / {self.country}/ {self.birthday} '

    def __repr__(self):
        return f'{self.fullname} / {self.country}/ {self.birthday} /{self.books}'

lib = Library('Mylib')
lib.new_book('War and Peace', 1900, Author('Tolstoy','Russia', 1828))
lib.new_book('Dead souls', 1835, Author('Gogol', 'Russia', 1809))
lib.new_book('Night before Christmas', 1832, Author('Gogol', 'Russia', 1809))


print(f'Библиотека: \n {lib}')

#for i in lib.authors:
#    print(f'seems*{i.fullname}*{i.country}*{i.birthday}*{i.books}')
#    print(f'{i.fullname} +++++  {i.books}')
for b in lib.books:
    print(f'Book = {b}')
print(lib.group_by_author('Gogol'))
print(lib.group_by_year(1900))

print(f'Всего книг в библиотеке = {Book.b_count}')
