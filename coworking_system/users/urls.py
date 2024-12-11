from tempfile import template

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import register_customer, register_owner

urlpatterns = [
    path('register/customer/', register_customer, name='register_customer'),
    path('register/owner/', register_owner, name='register_owner'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]