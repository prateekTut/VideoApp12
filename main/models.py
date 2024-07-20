from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from.manager import CustomUserManager
from django.contrib.auth import get_user_model
User = get_user_model()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()
    rating = models.CharField(max_length=30, null=True,blank=True)  # Assuming a simple integer rating system

    created_at = models.DateTimeField(auto_now_add=True)

 
    
class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.IntegerField()  # Assuming a simple integer rating system
    created_at = models.DateTimeField(auto_now_add=True)




