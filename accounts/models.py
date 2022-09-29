from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
    def __str__(self) -> str:
        return self.first_name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg',upload_to='profile_images')
    bio = models.TextField()
    def __str__(self) -> str:
        return self.user.username
    
    




