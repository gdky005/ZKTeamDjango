from django.db import models


# Create your models here.
from django.utils import timezone


class JDQSCategory(models.Model):
    categoryId = models.IntegerField(primary_key=True, default=1).auto_created
    categoryName = models.TextField(default="")
    categoryUrl = models.TextField(default="")
    artifactCollection = models.DateTimeField("CollectionTime", default=timezone.now)


class JDQSRecommendedCategory(models.Model):
    jId = models.IntegerField(primary_key=True, default=1).auto_created
    tjName = models.TextField(default="")
    tjUrl = models.TextField(default="")
    tjCollection = models.DateTimeField("CollectionTime", default=timezone.now)


class JDQSPicCategory(models.Model):
    picCategoryId = models.IntegerField(primary_key=True, default=1).auto_created
    picCategoryName = models.TextField(default="")
    picCategoryUrl = models.TextField(default="")
    picCategoryCollection = models.DateTimeField("CollectionTime", default=timezone.now)


class JDQSRecommendedItem(models.Model):
    id = models.IntegerField(primary_key=True, default=1).auto_created
    jid = models.TextField(default="")
    tjCategoryId = models.ForeignKey(JDQSRecommendedCategory)
    tjPicUrl = models.TextField(default="")
    tjName = models.TextField(default="")
    tjDate = models.DateTimeField(default=timezone.now)
    tjSourceUrl = models.TextField(default="")
    tjUrl = models.TextField(default="")
    tjCollection = models.DateTimeField("CollectionTime", default=timezone.now)


class JDQSItem(models.Model):
    id = models.IntegerField(primary_key=True, default=1).auto_created
    categoryId = models.ForeignKey(JDQSCategory)
    picUrl = models.TextField(default="")
    artifactName = models.TextField(default="")
    artifactDate = models.DateTimeField(default=timezone.now)
    artifactSourceUrl = models.TextField(default="")
    artifactUrl = models.TextField(default="")
    artifactCollection = models.DateTimeField("CollectionTime", default=timezone.now)


class JDQSPicUrl(models.Model):
    id = models.IntegerField(primary_key=True, default=1).auto_created
    picId = models.TextField(default=1)
    picCategoryId = models.ForeignKey(JDQSPicCategory)
    picUrl = models.TextField(default="")
    picTinyUrl = models.TextField(default="")
    picSmallUrl = models.TextField(default="")
    picZKUrl = models.TextField(default="")
    picName = models.TextField(default="")
    picCollection = models.DateTimeField("CollectionTime", default=timezone.now)


class JDQSContent(models.Model):
    id = models.IntegerField(primary_key=True, default=1).auto_created
    jid = models.ForeignKey(JDQSItem)
    artifactName = models.TextField(default="")
    artifactAuthor = models.TextField(default="")
    artifactContent = models.TextField(default="")
    artifactUrl = models.TextField(default="")
    artifactSourceUrl = models.TextField(default="")
    artifactCollection = models.DateTimeField("CollectionTime", default=timezone.now)
