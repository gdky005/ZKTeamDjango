from django.db import models


# Create your models here.
class UserInfo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=4)
