#from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all() #to retrieve all books from the db
    serializer_class = BookSerializer # use bookserializer to format data
