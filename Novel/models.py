from django.db import models


# Create your models here.
class NovelData(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    pid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()
