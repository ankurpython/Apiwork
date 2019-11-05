from django.db import models

class Dataset(models.Model):
    date=models.DateField(auto_now=False,auto_now_add=False)
    channel=models.CharField(max_length=100)
    country=models.CharField(max_length=12)
    os=models.CharField(max_length=25)
    impressions=models.IntegerField(default=0)
    clicks=models.IntegerField(default=0)
    installs=models.IntegerField(default=0)
    spend=models.DecimalField(max_digits=25,decimal_places=2)
    revenue=models.DecimalField(max_digits=25,decimal_places=2)
