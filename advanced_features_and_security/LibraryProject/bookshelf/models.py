#from django.db import models

# Create your models here.
#class Book(models.Model):
   # title = models.CharField(max_length=200)
    #author = models.CharField(max_length=100)
    #publication_year = models.IntegerField()

    #def __str__(self):
        #return self.title
    
from django.db import models   
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
from .models import CustomUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, password=None):
        if not email:
            raise ValueError('The Email must be filled')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, date_of_birth=date_of_birth)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, date_of_birth, password=None, **additional_attrs):
        additional_attrs.is_staff =True
        additional_attrs.is_superuser = True
        return self.create_user(email, username, date_of_birth, password,)

class CustomUser(AbstractUser):
     email = models.EmailField(unique=True)
     date_of_birth = models.DateField(null=True, blank=True)
     profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    

     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['profile_photo', 'date_of_birth']
    
     def __str__(self):
        return self.email
     

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.email