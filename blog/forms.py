from django import forms
from .models import Blog_main

class Blog_post_form(forms.ModelForm):
    class Meta:
        model = Blog_main
        fields = ['title', 'content', 'author', 'image']