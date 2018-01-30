from karbar.models import *
from madadkar.models import *
from madadju.models import *


class Hamyar(MyUser):
    report_method = models.IntegerField(choices={(0, 'text'), (1, 'email')})


class Message(models.Model):
    hamyar = models.ForeignKey(Hamyar, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    date = models.DateField()


class Payment(models.Model):
    date = models.DateField()
    payment_id = models.IntegerField( primary_key=True)
    value = models.IntegerField()
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)


class Adapt(models.Model):
    hamyar = models.ForeignKey(Hamyar, on_delete=models.CASCADE)
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
