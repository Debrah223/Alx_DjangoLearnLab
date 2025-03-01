from django.contrib import admin
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("publication_year")
    search_fields = ("title", "author")
# Register your models here.
admin.site.register(Book)


from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author")

# Function to set up groups with permissions
def setup_groups():
    content_type = ContentType.objects.get_for_model(Article)
    permissions = Permission.objects.filter(content_type=content_type)
    
    # Define groups
    editors, _ = Group.objects.get_or_create(name="Editors")
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    admins, _ = Group.objects.get_or_create(name="Admins")
    
    # Assign permissions
    editors.permissions.set(permissions.filter(codename__in=["can_edit", "can_create"]))
    viewers.permissions.set(permissions.filter(codename="can_view"))
    admins.permissions.set(permissions)