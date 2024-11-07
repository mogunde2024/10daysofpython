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

    def __str__(self):
        return self.title