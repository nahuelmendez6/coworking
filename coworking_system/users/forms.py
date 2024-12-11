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
        fields = ['firstname', 'lastname', 'username','password1','password2','company_name']
        labels = {
            'firstname':'Nombre',
            'lastname':'Apellido',
            'username':'Nombre de usuario',
            'password1':'Contraseña',
            'password2':'Repite la contraseña',
            'company_name':'Nombre de tu empresa'
        }

class CustomerRegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['firstname', 'lastname', 'username','password1','password2']
        labels = {
            'firstname':'Nombre',
            'lastname':'Apellido',
            'username':'Nombre de usuario',
            'password1':'Contraseña',
            'password2':'Repite la contraseña',
        }