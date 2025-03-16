from rest_framework import generics, permissions, filters
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

#we implement generic views
class BookListView(generics.ListAPIView):
    # we then retrieve all books
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #anyone can view the books

    # Add filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering by fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Search functionality (partial match for title and author)
    search_fields = ['title', 'author']

    # Ordering by fields (ascending and descending)
    ordering_fields = ['title', 'publication_year']

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
    

