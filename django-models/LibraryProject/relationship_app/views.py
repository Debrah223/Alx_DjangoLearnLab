from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    book_details = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(f"Books List:\n{book_details}")

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "libraru_detail.html" # this will be the template we shall use to render the output
    context_object_name = "library"