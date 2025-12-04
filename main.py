from library_manager.book import Book
from library_manager.inventory import LibraryInventory
import logging

logging.basicConfig(filename="library.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

inventory = LibraryInventory()

def add_book_cli():
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")

    book = Book(title, author, isbn)
    inventory.add_book(book)
    print("Book added successfully!")

def issue_book_cli():
    isbn = input("Enter ISBN to issue: ")
    book = inventory.search_by_isbn(isbn)

    if book and book.issue():
        inventory.save_data()
        print("Book issued!")
    else:
        print("Book not available!")

def return_book_cli():
    isbn = input("Enter ISBN to return: ")
    book = inventory.search_by_isbn(isbn)

    if book and book.return_book():
        inventory.save_data()
        print("Book returned!")
    else:
        print("You cannot return this book!")

def search_book_cli():
    title = input("Enter title to search: ")
    results = inventory.search_by_title(title)
    if results:
        for b in results:
            print(b)
    else:
        print("No matching books found.")

def view_all_cli():
    books = inventory.display_all()
    if not books:
        print("No books in library.")
    else:
        for b in books:
            print(b)

def menu():
    while True:
        print("\n===== Library Inventory Manager =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book_cli()
        elif choice == "2":
            issue_book_cli()
        elif choice == "3":
            return_book_cli()
        elif choice == "4":
            view_all_cli()
        elif choice == "5":
            search_book_cli()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid input. Try again!")

if __name__ == "__main__":
    menu()