from relationship_app import Author, Book, Library, Librarian

# Query to get all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        return Book.objects.filter(author=author)
    return None

# Query to list all books in a Library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name).first()
    if library:
        return library.books.all()
    return None

# Query to retrieve the librarian for a Library
def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return Librarian.objects.filter(library=library).first()
    return None