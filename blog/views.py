import markdown
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog_main
from .forms import Blog_post_form, CommentForm

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
    comments = post.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', post_id=post.id)
    else:
        form = CommentForm()
    post.content = markdown.markdown(post.content)  # Convert Markdown to HTML
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST["Username"]
        password = request.POST["Password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an erro loggin in, Try again!!!"))
            return redirect(login)
            
        
    else:
        return render(request, 'registration/login.html', {})



def add_post(request):
    if not request.user.is_authenticated:
        return redirect(f"{reverse('login')}?next={request.path}")
    if request.method == 'POST':
        
        form = Blog_post_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Blog_post_form()
    
    return render(request, 'add_post.html', {'form': form})


def edit_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect(f"{reverse('login')}?next={request.path}")
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
    if not request.user.is_authenticated:
        return redirect(f"{reverse('login')}?next={request.path}")
    post = get_object_or_404(Blog_main, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home') # redirect to the homepage after delection
    return render (request, 'post_confirm_delete.html', {'post': post})
