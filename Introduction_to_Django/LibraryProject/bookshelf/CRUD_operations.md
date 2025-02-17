# create operation
from bookshelf.models import Book
book = Book(title = "1984", author = "George Orwell", publication_year = 1949) 
book.save()
Book.objects.create

# retrieve operation
from bookshelf.models import Book
book = Book(title = "1984", author = "George Orwell", publication_year = 1949)
print(f"Title:{book.title}, Author:{book.author}, Year: {book.publication_year}")
# expected output
Title:1984, Author:George Orwell, Year: 1949

# update operation
from bookshelf.models import Book
book = Book.objects.get(title="1984")
# We convert book title from integer to string
book.title="Nineteen Eighty-Four" 
book.save()

# Adding delete operation
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
books=Book.objects.all()
print(books)