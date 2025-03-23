from django.urls import path
from blog import views
from .views import (
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView
    )
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
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
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), 
    path('profile/', views.profile, name='profile'),

    path("posts/", PostListView.as_view(), name="post-list"), # lists all posts
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"), #view a single post
    path("post/new/", PostCreateView.as_view(), name="post-create"),  #creates a new post
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # Edit a post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), # delete a post

    path("post/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-edit"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]