from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blog_main(models.Model):
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Content of the post
    author = models.CharField(max_length=200)  # type to a user
    created_date = models.DateTimeField(default=timezone.now)  # Auto-filled with current date/time
    updated_date = models.DateTimeField(auto_now=True)  # Updates with each save
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Blog_main, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"