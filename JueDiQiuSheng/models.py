from django.db import models


# Create your models here.

class JDQSCategory(models.Model):
    id = models.IntegerField(primary_key=True, default=1).auto_created
    categoryId = models.IntegerField(default=0)
    categoryName = models.TextField(default="")
    categoryUrl = models.URLField


class JDQSItem(models.Model):
    id = models.IntegerField(primary_key=True, default=1).auto_created
    jid = models.IntegerField()
    categoryId = models.ForeignKey(JDQSCategory)
    picUrl = models.URLField
    artifactName = models.TextField(default="")
    artifactDate = models.TextField(default="")


class JDQSContent(models.Model):
    id = models.IntegerField(primary_key=True, default=1).auto_created
    jid = models.ForeignKey(JDQSItem)
    artifactName = models.TextField(default="")
    artifactAuthor = models.TextField(default="")
    artifactContent = models.TextField(default="")
    artifactUrl = models.URLField
    artifactSourceUrl = models.URLField
