from django.db import models


class GKLQL(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    name = models.TextField()
    year = models.TextField()
    zyName = models.TextField()
    max = models.IntegerField()
    min = models.IntegerField()