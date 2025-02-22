from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library//<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from .views import register, user_login, user_logout

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views # import custom views


urlpatterns = [
    path("register/", views.register, name="register"),  # Registration page
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),  # Login page
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # Logout page
    path("", views.home, name="home"),  # Home page
]
