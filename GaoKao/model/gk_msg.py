from django.utils import timezone

from django.db import models


class GKMsgInfo(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    title = models.TextField()
    imgUrl = models.TextField()
    url = models.TextField(default="")
    uid = models.IntegerField(default=0)
    author = models.TextField(default="")
    summary = models.TextField(default="")
    des = models.TextField(default="")
    createTime = models.DateTimeField("createTime", default=timezone.now)

