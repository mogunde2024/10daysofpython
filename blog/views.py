import markdown
from django.shortcuts import render, get_object_or_404
from .models import Blog_main

# Create your views here.
def home_view(request):
    posts = Blog_main.objects.all().order_by('-created_date') # Fetch all posts, ordered by date (newest first)
    return render(request, 'home.html', {'posts': posts})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def post_detail(request, post_id):
    post = get_object_or_404(Blog_main, id=post_id) # fetch post or return a 404 if not found
    
    post.content = markdown.markdown(post.content)  # Convert Markdown to HTML
    return render(request, 'post_detail.html', {'post': post})