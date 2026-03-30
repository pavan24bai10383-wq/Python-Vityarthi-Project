from data_manager import library, save_library
from helper import get_valid_copies

def add_book():
    book_id = input("Enter Book ID: ").strip()
    if not book_id:
        print("Book ID cannot be empty!")
        return
    if book_id in library:
        print("Book already exists!")
        return

    title = input("Enter title: ").strip()
    if not title:
        print("Title cannot be empty!")
        return

    author = input("Enter author: ").strip()
    if not author:
        print("Author cannot be empty!")
        return

    copies = get_valid_copies(f"Enter number of copies of '{title}': ")

    library[book_id] = (title, author, copies)
    save_library()
    print(f"Book '{title}' added successfully!\n")


def display_books():
    if not library:
        print("No books available!\n")
        return

    print("\nLibrary Books")
    print("-" * 60)
    print(f"{'Book ID':<10}{'Title':<20}{'Author':<15}{'Copies':<6}")
    print("-" * 60)
    for book_id, (title, author, copies) in library.items():
        print(f"{book_id:<10}{title:<20}{author:<15}{copies:<6}")
    print()


def search_book():
    key = input("Enter Book ID to search: ").strip().lower()
    for book_id in library:
        if book_id.lower() == key:
            title, author, copies = library[book_id]
            print(f"\nBook Found!\nTitle: {title}\nAuthor: {author}\nCopies: {copies}\n")
            return
    print("Book not found!\n")


def update_copies():
    key = input("Enter Book ID to update: ").strip().lower()
    for book_id in library:
        if book_id.lower() == key:
            title, author, _ = library[book_id]
            new_copies = get_valid_copies("Enter new number of copies: ")
            library[book_id] = (title, author, new_copies)
            save_library()
            print("Book copies updated!\n")
            return
    print("Book not found!\n")


def delete_book():
    key = input("Enter Book ID to delete: ").strip().lower()
    for book_id in list(library.keys()):
        if book_id.lower() == key:
            del library[book_id]
            save_library()
            print("Book deleted!\n")
            return
    print("Book not found!\n")