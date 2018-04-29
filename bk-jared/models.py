from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.AutoField(max_length=128)
    blog_body = models.CharField(max_length=10240)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    
    



