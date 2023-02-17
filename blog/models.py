from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titel = models.CharField(max_length=250)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='')
    
    def __str__(self):
        return self.titel