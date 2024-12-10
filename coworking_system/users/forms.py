"""
Formularios de registro y autenticacion de usuarios
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        labels = {
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Correo electronico',
            'username':'Nombre de usuario',
            'password1':'Contraseña',
            'password2':'Repite contraseña'
        }