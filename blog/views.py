from django.shortcuts import render
from .models import Blog_main

# Create your views here.
def home_view(request):
    posts = Blog_main.objects.all().order_by('-created_date') # Fetch all posts, ordered by date (newest first)
    return render(request, 'home.html', {'posts': posts})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')