from django.db import models


# Create your models here.
class ManHua(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    jid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()

    class Meta:
        ordering = ['id']


class Category(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()

    class Meta:
        ordering = ['id']


class HotData(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    picUrl = models.TextField()
    newPage = models.TextField()

    class Meta:
        ordering = ['id']


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

    class Meta:
        ordering = ['id']


class MHDetailChapter(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()
    pCount = models.TextField()
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']


class MHChapterPic(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    mid2 = models.TextField()
    picUrl = models.TextField()
    count = models.IntegerField()
    sourceUrl = models.TextField()

    class Meta:
        ordering = ['id']

