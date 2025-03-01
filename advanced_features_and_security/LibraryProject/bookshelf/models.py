from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
    
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        permissions = [
            ("can_view", "Can view articles"),
            ("can_create", "Can create articles"),
            ("can_edit", "Can edit articles"),
            ("can_delete", "Can delete articles"),
        ]
    
    def __str__(self):
        return self.title
    
class CustomUser(AbstractUser):
     email = models.EmailField(unique=True)
     date_of_birth = models.DateField(null=True, blank=True)
     profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
     class Meta:
        permissions = [
            ("can_view", "Can view users"),
            ("can_create", "Can create users"),
            ("can_edit", "Can edit users"),
            ("can_delete", "Can delete users"),
        ]

#USERNAME_FIELD = 'email'
#REQUIRED_FIELDS = ['profile_photo', 'date_of_birth']
    
     def __str__(self):
        return self.email