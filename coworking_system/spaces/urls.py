from django.urls import path
from .views import new_space

urlpatterns = [
 path('new', new_space, name='new_space'),
]