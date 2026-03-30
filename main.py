from data_manager import load_library
from book_manager import add_book, display_books, search_book, update_copies, delete_book

load_library()

while True:
    print("""
==== Library Book Management System ====
1. Add Book
2. Display All Books
3. Search Book
4. Update Book Copies
5. Delete Book
6. Exit
""")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        update_copies()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.\n")