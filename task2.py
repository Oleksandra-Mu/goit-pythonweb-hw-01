from abc import ABC, abstractmethod
from logger import logger
from typing import List


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.library: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.library.append(book)
        logger.info(
            "Book added: Title: %s, Author: %s, Year: %s",
            book.title,
            book.author,
            book.year,
        )

    def remove_book(self, title: str) -> None:
        for book in self.library:
            if book.title == title:
                self.library.remove(book)
                logger.info("Book removed: %s", title)
                break
        else:
            logger.warning("Book not found: %s", title)

    def show_books(self) -> None:
        if not self.library:
            logger.info("У бібліотеці немає жодної книги.")
            return
        for book in self.library:
            logger.info(
                "Title: %s, Author: %s, Year: %s", book.title, book.author, book.year
            )


class LibraryManager:
    def __init__(self, library: Library) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = int(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
