from django.db import models


# Create your models here.
class VideoList(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    name = models.CharField(max_length=150)
    pic = models.CharField(max_length=1000)

