def view_all_books(all_books):
    if not all_books:
        print("No books available.")
        return
    print("\nAvailable Books:")
    for idx, book in enumerate(all_books, start=1):
        print(f"{idx}. Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
