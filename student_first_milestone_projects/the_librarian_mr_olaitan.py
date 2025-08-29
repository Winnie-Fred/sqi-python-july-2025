library = [
    {"title": "And then there were None", "author": "Agatha Christie", "year_of_publication": 1978, "isbn": "989-23-890-213", "available": True},
    {"title": "The Great Gatsby", "author": "Agatha Christie", "year_of_publication": 1978, "isbn": "989-23-890-213", "available": True},
    {"title": "The Shining", "author": "Stephen King", "year_of_publication": 1978, "isbn": "989-23-890-213", "available": False},
]

# library: list[dict[str, str | int]] = []

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
            print(f"""TItle: {book['title']}
Author: {book['author']}
Year of Publication: {book['year_of_publication']}
ISBN: {book['isbn']}
Available: {"Yes" if book["available"] else "No"}""")
            return
    print("Book not found")
    return

def update_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            print("Leave a field empty to keep it unchanged.")
            new_title = input(f"New title (current: {book['title']}): ")
            new_author = input(f"New author (current: {book['author']}): ")
            new_year = input(f"New year (current: {book['year_of_publication']}): ")
            book["title"] = new_title
            book["author"] = new_author
            book["year"] = new_year
            print("Book updated successfully")
            return
    print("Book not found")
    
    
def delete_book(isbn):
    global library
    initial_length = len(library)
    library = [book for book in library if book["isbn"] != isbn]
    if len(library) < initial_length:
        print("Book deleted successfully.\n")
    else:
        print("Book not found.\n")

def borrow_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            if book["available"]:
                book["available"] = False
                print("Book borrowed successfully.\n")
            else:
                print("Book is already borrowed.\n")
            return
    print("Book not found.\n")



def return_book(isbn):  
    for book in library:
        if book["isbn"] == isbn:
            if not book["available"]:
                book["available"] = True
                print("Book returned successfully.\n")
            else:
                print("Book is already available.\n")
            return
    print("Book not found.\n")   

menu = """1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Search Book
6. Borrow Book
7. Return Book
8. Exit"""



print("Welcome to the Community Library")
while True:
    print(menu)
    choice = input("Choose an option form the menu above: ").strip()
    if choice not in [str(num) for num in range(1, 9)]:
        print("Invalid choice")
        continue

    if choice == "8":
        print("Goodbye ðââï¸")
        break

    if choice == "1":
        print(add_book())
    elif choice == "2":
        view_books()
    elif choice == "5":
        title = input("Enter the title of the book you are searching for: ").strip()
        search_book(title)
    elif choice == "3":
        isbn = input("Enter ISBN of the book to update: ")
        update_book(isbn)
    elif choice == "4":
        isbn = input("Enter ISBN of the book to update: ")
        delete_book(isbn)
    elif choice == "6":
        isbn = input("Enter ISBN of the book to update: ")
        borrow_book(isbn)
    elif choice == "7":
        isbn = input("Enter ISBN of the book to update: ")
        return_book(isbn)