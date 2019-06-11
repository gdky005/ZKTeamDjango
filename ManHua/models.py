from django.db import models


# Create your models here.
class ManHua(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    jid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()


class Category(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()


class HotData(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    picUrl = models.TextField()
    newPage = models.TextField()


class MHDetail(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    author = models.TextField()
    picUrl = models.TextField()
    state = models.TextField()
    time = models.TextField()
    detail = models.TextField()
    category = models.TextField()
    tag = models.TextField()



