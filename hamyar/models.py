from django.db import models
from karbar.models import *


class Hamyar(MyUser):
    report_method = models.CharField(choices={(0, 'text'), (1, 'email')})


# TODO
# class Message(models.Model):
#     hamyar = models.ForeignKey(Hamyar, on_delete=models.CASCADE)
#     title = models.CharField(max_length=50)
#     content = models.CharField(max_length=1000)
#     date = models.DateField()
#     receiver = models.ForeignKey(ExecutiveManager, on_delete=models.CASCADE)
#
#
# class Payment(models.Model):
#     date = models.DateField()
#     payment_id = models.IntegerField(max_length=10, primary_key=True)
#     value = models.IntegerField(max_length=100)
#     madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
#
#
# class Adapt(models.Model):
#     id = models.IntegerField(max_length=10, primary_key=True)
#     hamyaar = models.ForeignKey(Hamyaar, on_delete=models.CASCADE)
#     madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
