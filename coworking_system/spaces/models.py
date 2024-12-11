from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=100)

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Province(models.Model):
    province_name = models.CharField(max_length=100)