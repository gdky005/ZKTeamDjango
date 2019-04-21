from django.db import models


# Create your models here.
class GKUserInfo(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    uid = models.IntegerField()
    name = models.TextField()
    phone = models.TextField()