def update_book(all_books):
    title = input("Enter the title of the book to update: ")
    for book in all_books:
        if book["title"].lower() == title.lower():
            new_author = input("Enter the new author (or press Enter to keep unchanged): ")
            new_quantity = input("Enter the new quantity (or press Enter to keep unchanged): ")
            if new_author:
                book["author"] = new_author
            if new_quantity.isdigit():
                book["quantity"] = new_quantity
            print(f"Book '{title}' updated successfully.")
            return all_books
    print("Book not found.")
    return all_books
