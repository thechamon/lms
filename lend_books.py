import datetime
import json

LEND_BOOK_FILE = "lend_books.json"

def initialize_lend_books_file():
    try:
        with open(LEND_BOOK_FILE, "x") as file:
            json.dump([], file)
    except FileExistsError:
        pass

def lend_book(all_books):
    title = input("Enter the title of the book to lend: ")
    for book in all_books:
        if book["title"].lower() == title.lower():
            if int(book["quantity"]) > 0:
                name = input("Enter borrower's name: ")
                phone = input("Enter borrower's phone number: ")
                due_date = datetime.datetime.now() + datetime.timedelta(days=14)

                with open(LEND_BOOK_FILE, "r") as file:
                    lend_records = json.load(file)

                lend_records.append({
                    "name": name,
                    "phone": phone,
                    "title": title,
                    "due_date": due_date.strftime("%Y-%m-%d")
                })

                with open(LEND_BOOK_FILE, "w") as file:
                    json.dump(lend_records, file)

                book["quantity"] = str(int(book["quantity"]) - 1)
                print(f"Book '{title}' lent successfully. Due date: {due_date.strftime('%Y-%m-%d')}")
                return all_books
            else:
                print("There are not enough books available to lend.")
                return all_books
    print("No book found with the given title.")
    return all_books

def return_book(all_books):
    title = input("Enter the title of the book to return: ")
    name = input("Enter borrower's name: ")

    with open(LEND_BOOK_FILE, "r") as file:
        lend_records = json.load(file)

    updated_lend_records = []
    found = False

    for record in lend_records:
        if record["title"].lower() == title.lower() and record["name"] == name:
            for book in all_books:
                if book["title"].lower() == title.lower():
                    book["quantity"] = str(int(book["quantity"]) + 1)
                    print(f"Book '{title}' returned successfully.")
                    found = True
                    break
        else:
            updated_lend_records.append(record)

    if not found:
        print("No matching lend record found.")

    with open(LEND_BOOK_FILE, "w") as file:
        json.dump(updated_lend_records, file)

    return all_books
