from django import forms
from .models import Blog_main, Comment

class Blog_post_form(forms.ModelForm):
    class Meta:
        model = Blog_main
        fields = ['title', 'content', 'author', 'image']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']