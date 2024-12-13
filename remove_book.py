def remove_book(all_books):
    title = input("Enter the title of the book to remove: ")
    for book in all_books:
        if book["title"].lower() == title.lower():
            all_books.remove(book)
            print(f"Book '{title}' removed successfully.")
            return all_books
    print("Book not found.")
    return all_books
