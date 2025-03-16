# serializers
from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer): #serializes all fields of the book model. 
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
         # This is custom validation to ensure that publication year is not in the future
         current_year = datetime.now().year
         if value > current_year:
             raise serializers.ValidationError("Publication yearcannot be in the future.")
         return value
    
class AuthorSerializer(serializers.ModelSerializer): #includes the name field
    books = BookSerializer(many=True, read_only=True) #we are adding a nested serialization to include related books dynamically

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
    