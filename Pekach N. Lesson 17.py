# Lesson 17
## Task 1

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return "Woof-woof!"

class Cat(Animal):
    def talk(self):
        return "Meow!"

def animal_sound(animal: Animal):
    print(animal.talk())

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)

## Task 2

class Author:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date
        self.books = []

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birth_date='{self.birth_date}')"

    def __str__(self):
        return f"{self.name}, {self.country} (Born: {self.birth_date})"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={self.author.name})"

    def __str__(self):
        return f"'{self.name}' by {self.author.name} ({self.year})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f"Library(name='{self.name}', books={self.books}, authors={self.authors})"

    def __str__(self):
        return f"Library: {self.name} (Books: {len(self.books)})"

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]


author1 = Author("J.K. Rowling", "UK", "1965-07-31")
author2 = Author("George Orwell", "UK", "1903-06-25")

library = Library("City Library")
book1 = library.new_book("Harry Potter and the Philosopher's Stone", 1997, author1)
book2 = library.new_book("1984", 1949, author2)
book3 = library.new_book("Harry Potter and the Chamber of Secrets", 1998, author1)

print(library)
print(library.group_by_author(author1))
print(library.group_by_year(1997))
print(f"Total books in library: {Book.total_books}")

## Task 3

import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ValueError("Cannot divide by zero")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return NotImplemented

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    result = x + y
    print(result)
