from django.db import models


# Create your models here.
class ProjectInfo(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    name = models.CharField(max_length=50)
    pic = models.CharField(max_length=1000)
    address = models.CharField(max_length=250)
    des = models.CharField(max_length=1000)
