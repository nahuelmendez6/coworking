from django.db import models
from django.db.models import CASCADE
from importlib import import_module

#from coworking_system.users.models import CustomUser

#from users.models import CustomUser
#from users.models import CustomUser
# Create your models here.
CustomUser = import_module('users.models').CustomUser

# Space settings models

class City(models.Model):
    city_name = models.CharField(max_length=100)

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Province(models.Model):
    province_name = models.CharField(max_length=100)

class Hour(models.Model):
    hour = models.CharField(max_length=50)

class Day(models.Model):
    day = models.CharField(max_length=50)

class SpaceAddress(models.Model):

    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10, blank=True, null=True)
    floor = models.CharField(max_length=10, blank=True, null=True)
    apartment = models.CharField(max_length=10, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    city = models.ForeignKey(
        City,
        on_delete=CASCADE,
        related_name="city"

    )
    department = models.ForeignKey(
        Department,
        on_delete=CASCADE,
        related_name="department"
    )
    province = models.ForeignKey(
        Department,
        on_delete=CASCADE,
        related_name="province"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Space(models.Model):

    name = models.CharField(max_length=100)
    description = models.TimeField(blank=True, null=True)
    capacity = models.PositiveIntegerField()
    address = models.ForeignKey(
        SpaceAddress,
        on_delete=CASCADE,
        related_name="address"
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="spaces"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Amenity(models.Model):

    space = models.ForeignKey(
        Space,
        on_delete=CASCADE,
        related_name="amenities"
    )
    name = models.CharField(max_length=100, unique=True,blank=True ,null=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Room(models.Model):

    space = models.ForeignKey(
        Space,
        on_delete=CASCADE,
        related_name="rooms"
    )
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):

    space = models.ForeignKey(
        Space,
        on_delete=CASCADE,
        related_name="reviews"
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name="userReview"
    )
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SpaceImage(models.Model):
    space = models.ForeignKey(
        Space,
        on_delete=CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to='spaces/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WorkingHours(models.Model):

    space = models.ForeignKey(
        Space,
        on_delete=CASCADE,
        related_name="workingHours"
    )
    day = models.ForeignKey(
        Day,
        on_delete=CASCADE,
        related_name="days"
    )
    fromHour = models.ForeignKey(
        Hour,
        on_delete=CASCADE,
        related_name="fromHour"
    )
    untilHour = models.ForeignKey(
        Hour,
        on_delete=CASCADE,
        related_name="untilHour"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


