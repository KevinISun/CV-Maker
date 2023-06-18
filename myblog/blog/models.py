from django.db import models

# Create your models here.
# Added below
class Post(models.Model):
    username = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class JdPost(models.Model):
    url = models.CharField(max_length=300)
    # url = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)