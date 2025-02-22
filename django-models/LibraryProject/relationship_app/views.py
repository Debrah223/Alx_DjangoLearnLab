from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html" # this will be the template we shall use to render the output
    context_object_name = "library"