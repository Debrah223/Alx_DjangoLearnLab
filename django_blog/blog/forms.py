from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Tag
from .models import Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas",
    )
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]  # Exclude 'author' because it's set automatically

    def save(self, commit=True):
        post = super().save(commit=False)
        tag_names = self.cleaned_data['tags'].split(',')
        tag_objects = [Tag.objects.get_or_create(name=tag.strip())[0] for tag in tag_names if tag.strip()]
        if commit:
            post.save()
            post.tags.set(tag_objects)
        return post

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        return content
