from django.db import models


# Create your models here.
class ShopInfo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    pid = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    des = models.CharField(max_length=50)
