from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet, CustomAuthToken


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all') #creates api book endpoint

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'), # Maps to the BookList view
    path('', include(router.urls)),  #to include all router generated  urls
    path('api/token/', CustomAuthToken.as_view(), name='api_token_auth'),
]