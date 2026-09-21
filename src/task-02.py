import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Book:
    title: str
    author: str
    year: str

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def get_books(self) -> list[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> bool:
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                return True
        return False

    def get_books(self) -> list[Book]:
        return list(self._books)


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logger.info("Book added: %s", book)

    def remove_book(self, title: str) -> None:
        if self.library.remove_book(title):
            logger.info("Book removed: %s", title)
        else:
            logger.info("Book not found: %s", title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logger.info("Library is empty")
            return
        for book in books:
            logger.info("%s", book)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
