from django.db import models


class GKZY(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    name = models.TextField()
    bigName = models.TextField()
    xueli = models.TextField()