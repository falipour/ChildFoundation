from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    username = models.CharField(max_length=30, primary_key=True, default='')
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    password = models.CharField(max_length=10, default='')
    national_id = models.IntegerField(unique=True, blank=True)

    # address
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    postal_code = models.IntegerField()

    phone_number = models.IntegerField()

