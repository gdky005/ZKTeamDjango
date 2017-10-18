from django.db import models


# Create your models here.

class JDQSCategory(models.Model):
    categoryId = models.IntegerField(primary_key=True, default=1).auto_created
    categoryName = models.TextField(default="")
    categoryUrl = models.TextField(default="")


class JDQSItem(models.Model):
    jid = models.IntegerField(primary_key=True, default=1).auto_created
    categoryId = models.ForeignKey(JDQSCategory)
    picUrl = models.TextField(default="")
    artifactName = models.TextField(default="")
    artifactDate = models.TextField(default="")
    artifactSourceUrl = models.TextField(default="")
    artifactUrl = models.TextField(default="")


class JDQSContent(models.Model):
    id = models.IntegerField(primary_key=True, default=1).auto_created
    jid = models.ForeignKey(JDQSItem)
    artifactName = models.TextField(default="")
    artifactAuthor = models.TextField(default="")
    artifactContent = models.TextField(default="")
    artifactUrl = models.TextField(default="")
    artifactSourceUrl = models.TextField(default="")
