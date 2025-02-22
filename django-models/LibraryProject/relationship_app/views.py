from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

from django.views.generic.detail import DetailView
from .models import Library

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "relationship_app/home.html")


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html" # this will be the template we shall use to render the output
    context_object_name = "library"


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home") #redirect user to homepage
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})
    
def user_logout(request):
    logout(request)
    return redirect("login")

