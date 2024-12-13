def add_books(all_books):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    quantity = input("Enter the quantity of the book: ")
    if not quantity.isdigit():
        print("Invalid quantity. Please enter a number.")
        return all_books
    all_books.append({"title": title, "author": author, "quantity": quantity})
    print(f"Book '{title}' added successfully.")
    return all_books
