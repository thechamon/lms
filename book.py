import add_books
import view_all_books
import update_book
import remove_book
import save_all_books
import lend_books

all_books = save_all_books.load_books_from_file()
lend_books.initialize_lend_books_file()

while True:
    print("\nWelcome to Library Management System")
    print("0. Exit")
    print("1. Add Book")
    print("2. View all Books")
    print("3. Update a Book")
    print("4. Remove a Book")
    print("5. Lend a Book")
    print("6. Return a Book")

    menu = input("Select any number: ")

    if menu == "0":
        save_all_books.save_books_to_file(all_books)
        print("Thanks for using Library Management System.")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        all_books = update_book.update_book(all_books)
    elif menu == "4":
        all_books = remove_book.remove_book(all_books)
    elif menu == "5":
        all_books = lend_books.lend_book(all_books)
    elif menu == "6":
        all_books = lend_books.return_book(all_books)
    else:
        print("Invalid option. Please try again.")
