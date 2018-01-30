from karbar.models import *


class Madadkar(MyUser):
    employment_date = models.DateField(null=True, blank=True)


class Receipt(models.Model):
    madadkar = models.ForeignKey(Madadkar, on_delete=models.CASCADE)
    hamyar = models.ForeignKey('hamyar.Hamyar', on_delete=models.CASCADE)
    madadju = models.ForeignKey('madadju.Madadju', on_delete=models.CASCADE)
    date_receive = models.DateField()
    date_send = models.DateField()
    content = models.CharField(max_length=500)
