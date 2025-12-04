import logging

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__status = status  # available / issued

    def __str__(self):
        return f"{self.__title} by {self.__author} | ISBN: {self.__isbn} | Status: {self.__status}"

    # Encapsulation Getters
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def status(self):
        return self.__status

    # Methods
    def is_available(self):
        return self.__status == "available"

    def issue(self):
        if self.is_available():
            self.__status = "issued"
            logging.info(f"Book issued: {self.__title}")
            return True
        return False

    def return_book(self):
        if not self.is_available():
            self.__status = "available"
            logging.info(f"Book returned: {self.__title}")
            return True
        return False

    def to_dict(self):
        return {
            "title": self.__title,
            "author": self.__author,
            "isbn": self.__isbn,
            "status": self.__status
        }