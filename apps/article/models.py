from PIL import Image
from django.core.files import File
from io import BytesIO


from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='post', null='False')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images')
    thumbnail = models.ImageField(upload_to='post_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.set_thumbnail()
        super().save(*args, **kwargs)
    
    def set_thumbnail(self):
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
                
            thumb_io = BytesIO()
            img.save(thumb_io, format='UPEG', quality=85)
                
            file_name = self.image.name.split('/')[-1]
            self.thumbnail.save(file_name, File(thumb_io), save=False)
        
    def get_thumbnail(self):
        if not self.thumbnail:
            self.set_thumbnail()
        return self.thumbnail.url
                