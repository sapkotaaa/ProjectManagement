import imp
from pyexpat import model
from socket import fromshare
from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email']
        