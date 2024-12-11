from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    is_provider = models.BooleanField(default=False)
    company_name = models.CharField(max_length=100, blank=True, null=True)

