from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the author of a post or comment to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions for GET, HEAD, OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the owner of the object
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    """
    API view to handle CRUD operations for posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'content']  # Allows users to search by title or content


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Assign the logged-in user as the author

class CommentViewSet(viewsets.ModelViewSet):
    """
    API view to handle CRUD operations for comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Assign the logged-in user as the author

