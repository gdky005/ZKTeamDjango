from django.db import models


# Create your models here.

class JDQSCategory(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    jid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()
    picUrl = models.TextField()
    categoryId = models.TextField(default="")
    categoryName = models.TextField(default="")
