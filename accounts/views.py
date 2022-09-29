from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.




    
    
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/register.html"
    
