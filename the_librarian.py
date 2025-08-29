# library = [
#     {"title": "And then there were None", "author": "Agatha Christie", "year_of_publication": 1978, "isbn": "989-23-890-213", "available": True},
#     {"title": "The Great Gatsby", "author": "Agatha Christie", "year_of_publication": 1978, "isbn": "989-23-890-213", "available": True},
#     {"title": "The Shining", "author": "Stephen King", "year_of_publication": 1978, "isbn": "989-23-890-213", "available": False},
# ]

library: list[dict[str, str | int]] = []

def add_book():
    title = input("Enter the title of the book you want to add: ").strip()
    author = input("Enter the author of the book: ").strip()
    year_of_publication = int(input("Enter the year of publication of the book: "))
    isbn = input("Enter the ISBN of the book: ").strip()
    book = {"title": title, "author": author, "year_of_publication": year_of_publication, "isbn": isbn, "available": True}
    library.append(book)
    return "Book added successfully"




def view_books():
    if library:
        for idx, book in enumerate(library, start=1):
            print(f"\n\nBook {idx}:")
            print(f"""TItle: {book['title']}
Author: {book['author']}
Year of Publication: {book['year_of_publication']}
ISBN: {book['isbn']}
Available: {"Yes" if book["available"] else "No"}""")
    else:
        print("No books in the library, check back later.")



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

    if choice == "8":
        print("Good bye 👋")
        break

    if choice == "1":
        print(add_book())
    elif choice == "2":
        view_books()
    elif choice == "5":
        title = input("Enter the title of the book you are searching for: ").strip()
        search_book(title)