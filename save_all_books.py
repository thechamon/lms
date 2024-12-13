import json

BOOK_FILE = "all_books.json"

def save_books_to_file(all_books):
    with open(BOOK_FILE, "w") as file:
        json.dump(all_books, file)
    print("Books saved successfully.")

def load_books_from_file():
    try:
        with open(BOOK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
