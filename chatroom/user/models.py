from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True,null=True)
    bio=models.TextField(null=True)
    mobile=models.CharField(max_length=10,null=True)
    avatar=models.ImageField(null=True,default='default_user.png')

    def __str__(self):
        return self.username

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]