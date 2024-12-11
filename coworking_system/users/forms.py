"""
Formularios de registro y autenticacion de usuarios
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CustomUser


class OwnerRegistratrionForm(UserCreationForm):

    company_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','email' ,'username','password1','password2','company_name']
        labels = {
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email': 'Email',
            'username':'Nombre de usuario',
            'password1':'Contraseña',
            'password2':'Repite la contraseña',
            'company_name':'Nombre de tu empresa'
        }

class CustomerRegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','email' ,'username','password1','password2']
        labels = {
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Email',
            'username':'Nombre de usuario',
            'password1':'Contraseña',
            'password2':'Repite la contraseña',
        }