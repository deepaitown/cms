from django.db import models
from django.conf import settings

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=50,null=False,blank=False)
    body = models.TextField(max_length=5000,null=False,blank=False)
    image = models.ImageField(upload_to=r'C:\Users\jayarame\Documents\Django_project\cms\images',null=False,blank=False)
    date_published = models.DateTimeField(auto_now_add=True,verbose_name="date published")
    date_updated = models.DateTimeField(auto_now_add=True,verbose_name="date updated")
    comments = models.TextField(max_length=5000,null=False,blank=False)

    def __str__(self):
        return self.title