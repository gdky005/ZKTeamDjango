from django.db import models


class GKListInfo(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    title = models.TextField()
    imgUrl = models.TextField()
    url = models.TextField()

