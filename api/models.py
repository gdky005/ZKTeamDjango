from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField
    sex = models.CharField(max_length=4)
