from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


#router = DefaultRouter()
#router.register(r'books_all', BookViewSet, basename='book_all') #creates api book endpoint

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]