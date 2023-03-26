from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    introduce = models.TextField()
    Email = models.EmailField(max_length=100, blank=True)
    image = models.ImageField(upload_to='blog_img', blank=True)

    def __str__(self):
        return self.title