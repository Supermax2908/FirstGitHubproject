from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='post', null='False')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images')
    like = models.ManyToManyField(User, related_name='like_posts', blank=True)
    dislike = models.ManyToManyField(User, related_name='dislike_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
                