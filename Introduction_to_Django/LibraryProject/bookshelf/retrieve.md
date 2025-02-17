from bookshelf.models import Book
book = Book(title = "1984", author = "George Orwell", publication_year = 1949)
print(f"Title:{book.title}, Author:{book.author}, Year: {book.publication_year}")
Book.objects.get
# expected output
Title:1984, Author:George Orwell, Year: 1949