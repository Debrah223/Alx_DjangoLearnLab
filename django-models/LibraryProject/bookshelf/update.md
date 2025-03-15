from bookshelf.models import Book
book = Book.objects.get(title="1984")
# We convert book title from integer to string
book.title="Nineteen Eighty-Four" 
book.save()