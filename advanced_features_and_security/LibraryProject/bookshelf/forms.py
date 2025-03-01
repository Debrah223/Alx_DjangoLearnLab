from django import forms
from .models import Book  # Add a  Book model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date'] 