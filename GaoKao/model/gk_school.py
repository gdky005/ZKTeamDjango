from django.db import models


class GKSchool(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    name = models.TextField()
    logoUrl = models.TextField()
    url = models.TextField(default="")
    city = models.TextField()