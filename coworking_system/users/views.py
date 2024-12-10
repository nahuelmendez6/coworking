from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.

class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')