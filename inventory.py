import json
import logging
from pathlib import Path
from .book import Book

class LibraryInventory:
    def __init__(self, file_path="data/books.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_data()

    def load_data(self):
        """Load books from JSON with exception handling."""
        try:
            if self.file_path.exists():
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    for item in data:
                        self.books.append(Book(**item))
            else:
                self.save_data()
        except Exception as e:
            logging.error("Error loading data: %s", e)
            self.books = []

    def save_data(self):
        """Save books to JSON."""
        try:
            with open(self.file_path, "w") as file:
                json.dump([book.to_dict() for book in self.books], file, indent=4)
        except Exception as e:
            logging.error("Failed to save data: %s", e)

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        return self.books