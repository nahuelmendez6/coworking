from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    #first_name = models.CharField(max_length=100, blank=True, null=True)
    #last_name = models.CharField(max_length=100, blank=True, null=True)
    is_provider = models.BooleanField(default=False)
    company_name = models.CharField(max_length=100, blank=True, null=True)

