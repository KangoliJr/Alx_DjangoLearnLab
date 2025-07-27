from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
def books_by_author(author_name):
    author =Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"{book.title}")
        
# List all books in a library.
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in the library {library_name}")
    for book in books:
        print(f"{book.title}")
        
# Retrieve the librarian for a library.
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"The librarian for {library_name} is {librarian.name}")