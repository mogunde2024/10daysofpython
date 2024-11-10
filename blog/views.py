import markdown
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog_main
from .forms import Blog_post_form

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

def add_post(request):
    if request.method == 'POST':
        form = Blog_post_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Blog_post_form()
    
    return render(request, 'add_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Blog_main, id=post_id)
    if request.method == 'POST':
        form = Blog_post_form(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', post_id=post.id)
    else:
        form = Blog_post_form(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

def post_delete(request, post_id):
    post = get_object_or_404(Blog_main, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home') # redirect to the homepage after delection
    return render (request, 'post_confirm_delete.html', {'post': post})
