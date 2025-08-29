library = [
    {"title": "And then there were None", "author": "Agatha Christie", "year_of_publication": 1978, "isbn": "989-23-890-210", "available": True},
    {"title": "The Great Gatsby", "author": "Agatha Christie", "year_of_publication": 1978, "isbn": "989-23-890-210", "available": True},
    {"title": "The Shining", "author": "Stephen King", "year_of_publication": 1978, "isbn": "989-23-890-212", "available": False},
]
def add_book():
    title = input("Enter the title of the book you want to add: ").strip()
    author = input("Enter the author of the book: ").strip()
    year_of_publication = input("Enter the year of publication of the book: ").strip()
    isbn = input("Enter the ISBN of the book: ").strip()
    book = {"title": title, "author": author, "year_of_publication": year_of_publication, "isbn": isbn, "available": True}
    library.append(book)
    return "Book added successfully"

def view_books():

    if not library:
        print("\nNo books in the library\n")
        return

    for idx, book in enumerate(library, start=1):
        print(f"\n\nBook {idx}:")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Year Published: {book['year_of_publication']}")
        print(f"ISBN: {book['isbn']}")
        print("Available:", f"Yes" if book["available"] else "No")
    return

def search_book(title: str):
    for book in library:
        if book['title'].lower() == title.lower():
            print("Book found")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year Published: {book['year_of_publication']}")
            print(f"ISBN: {book['isbn']}")
            print("Available:", f"Yes" if book["available"] else "No")
            return
    print("Book not found")
    return

def update_book(isbn: str):
    for book in library:
        if book['isbn'] == isbn:
            new_title = input("Enter new title: ").strip()
            author = input("Enter new author: ").strip()
            year_of_publication = input("Enter the new year of the book: ").strip()
            new_isbn = input("Enter the new ISBN of the book: ").strip()

            book["title"] = new_title
            book["author"] = author
            book["year_of_publication"] = year_of_publication
            book["isbn"] = new_isbn
            print("Book updated successfully")
            return
        print("Book not found")

# def delete_book(isbn: str):
#     for idx, book in enumerate(library):
#         if book['isbn'] == isbn:
#             del library[idx]
#             print("Successfully deleted the book")
#             return
#     print("Book does not exist")


# def delete_book(isbn: str):
#     for book in library:
#         if book['isbn'] == isbn:
#             library.remove(book)
#             print("Successfully deleted the book")
#             return
#     print("Book does not exist")

# def delete_book(isbn: str):
#     for idx, book in enumerate(library):
#         if book['isbn'] == isbn:
#             library.pop(idx)
#             print("Successfully deleted the book")
#             return
#     print("Book does not exist")


def delete_book(isbn: str):
    global library
    new_library = []
    for book in library:
        if book['isbn'] != isbn:
            new_library.append(book)
    deleted = len(library) != len(new_library)
    print(f"Books with ISBN {isbn} deleted" if deleted else "No book witht hat ISBN exists.")
    library = new_library


def borrow_book(isbn: str):
    for book in library:
        if book['isbn'] == isbn:
            if book["available"] == False:
                print("Book has already been borrowed")
                return
            book["available"] = False
            print("Please make sure to return soon. Have a good read...")
            return
    print("We dont have that book")

def return_book(isbn: str):
    for book in library:
        if book['isbn'] == isbn:
            if book["available"] == True:
                print("This book is already in our collection")
                return
            book["available"] = True
            print("Thank you for choosing our library. We hope you enjoyed your time reading")
            return
    print("We dont have a record of the book you want to return, the book is not ours")

menu = """1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Search Book
6. Borrow Book
7. Return Book
8. Exit"""

print("Welcome to Dugbe Community Library!")
header = """
#########################
#     DUGBE LIBRARY     #   
#########################
"""
print(header)
while True:
    print(menu)
    choice = input("Choose an option from the menu above: ").strip()

    if choice not in [str(num) for num in range(1, 9)]:
        print("Invalid choice")
        continue

    if choice == "8":
        print("Goodbye 🙋‍♀️")
        break

    if choice == "1":
        print(add_book())
    elif choice == "2":
        view_books()
    elif choice == "5":
        title = input("Enter the title of the book you are searching for: ").strip()
        search_book(title)
    elif choice == "3":
        isbn = input("Enter the isbn of the book you want to edit: ").strip()
        update_book(isbn)
    elif choice == "4":
        isbn = input("Enter the isbn of the book you want to delete: ").strip()
        delete_book(isbn)
    elif choice == "6":
        isbn = input("Enter the isbn of the book you want to borrow: ").strip()
        borrow_book(isbn)
    elif choice == "7":
        title = input("Enter the title of the book you want to return: ").strip()
        return_book(title)

