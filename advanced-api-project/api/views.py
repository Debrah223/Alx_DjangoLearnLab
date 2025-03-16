from rest_framework import generics, permissions
from .serializers import BookSerializer
from .models import Book

#we implement generic views
class BookListView(generics.ListAPIView):
    # we then retrieve all books
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #anyone can view the books

class BookDetailView(generics.RetrieveAPIView):
    # retrieve a single book by ID
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #anyone can view the details

class BookCreateView(generics.CreateAPIView):
    # to create a new book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # only autheticated user

class BookUpdateView(generics.UpdateAPIView):
    # to update existing view
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] #only autheticated user

class BookDeleteView(generics.DeleteAPIView):
    # to delete a book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] #only autheticated user
    

