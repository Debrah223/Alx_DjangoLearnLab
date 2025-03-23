from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path("", PostListView.as_view(), name="post-list"), # lists all posts
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"), #view a single post
    path("post/new/", PostCreateView.as_view(), name="post-create"),  #creates a new post
     path("posts/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), # delete a post
]