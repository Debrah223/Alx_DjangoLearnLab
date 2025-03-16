Summary of Implementation:
Views:

BookListView: Retrieves all books (read-only, public).
BookDetailView: Retrieves a single book by ID (read-only, public).
BookCreateView: Creates a book (authenticated users only).
BookUpdateView: Updates a book (authenticated users only).
BookDeleteView: Deletes a book (authenticated users only).

Permissions:

AllowAny: For listing and retrieving books.
IsAuthenticated: Required for creating, updating, and deleting books.

URL Patterns:

/books/: Lists all books.
/books/<int:pk>/: Retrieves details of a specific book.
/books/create/: Adds a new book (authenticated users only).
/books/update/<int:pk>/: Updates a book (authenticated users only).
/books/delete/<int:pk>/: Deletes a book (authenticated users only).