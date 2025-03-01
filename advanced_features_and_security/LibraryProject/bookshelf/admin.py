#from django.contrib import admin
#from .models import Book
#class BookAdmin(admin.ModelAdmin):
    #list_display = ("title", "author", "publication_year")
    #list_filter = ("publication_year")
    #search_fields = ("title", "author")
# Register your models here.
#admin.site.register(Book)

from django.contrib import admin
from .models import CustomUser  # Import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_of_birth', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

admin.site.register(CustomUser, CustomUserAdmin) #registering custom user
