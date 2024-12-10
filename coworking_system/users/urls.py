from tempfile import template

from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template='logout.html'), name='logout'),
]