from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_id = models.IntegerField(unique=True, blank=True)

    # address
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    postal_code = models.IntegerField()

    phone_number = models.IntegerField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

