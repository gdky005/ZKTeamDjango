from django.db import models


# Create your models here.
class NovelData(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    pid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()
    sourceUrl = models.TextField(default="")


class NovelDetailData(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    pid = models.IntegerField()
    name = models.TextField()
    author = models.TextField()
    content = models.TextField()
    url = models.TextField()
    sourceUrl = models.TextField()
